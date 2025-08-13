import os, re
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    usr = db.execute("SELECT username, cash FROM users WHERE id = ?", session.get("user_id"))
    username = usr[0]["username"]
    cash = usr[0]["cash"]

    data = db.execute("SELECT stock, balance FROM stockbalance\
                       WHERE balance > 0 AND username = ? ORDER BY stock", username)

    stocks = []
    total_assets = 0
    if data != []:
        for row in data:
            temp = {}
            temp["symbol"] = row["stock"]
            temp["shares"] = row["balance"]
            stock = lookup(row["stock"])
            temp["name"] = stock["name"]
            temp["price"] = usd(stock["price"])
            temp["total"] = usd(stock["price"] * row["balance"])
            total_assets = total_assets + (stock["price"] * row["balance"])
            stocks.append(temp)
        total_assets = total_assets + cash
    else:
        total_assets = cash

    return render_template("index.html", stocks=stocks, cash=usd(cash), totalAssets=usd(total_assets))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol_entered = request.form.get("symbol")
        shares_entered = request.form.get("shares")

        if not symbol_entered:
            return apology("must provide Stock symbol", 400)

        stock = lookup(symbol_entered)

        if stock == None:
            return apology("Stock symbol not found", 400)

        if not shares_entered:
            return apology("must provide a number of shares to buy", 400)

        pattern = r'^[1-9]\d*$'
        if not re.search(pattern, shares_entered):
            return apology("Number of shares must by a positive integer", 400)

        shares = int(shares_entered)

        data = db.execute("SELECT username, cash FROM users WHERE id = ?", session.get("user_id"))
        cash = data[0]["cash"]
        username = data[0]["username"]
        price = float(stock["price"])
        total = shares * price

        if cash < total:
            return apology(f"Price {usd(price)} X {shares} shares = {usd(total)} is more than {usd(cash)} available", 403)

        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        formatted_time = now.strftime("%H:%M:%S")
        date_time = formatted_date + " " + formatted_time

        db.execute("INSERT INTO stocks (username, stock, opdate, qty, price, operation) VALUES (?,?,?,?,?,?)",\
                    username, symbol_entered, date_time, shares, price, 'B')

        own = db.execute("SELECT balance from stockbalance \
                   WHERE username = ? and stock = ?", username, symbol_entered)
        if own == []:
            db.execute("INSERT INTO stockbalance (username, stock, balance) VALUES (?,?,?)", \
                       username, symbol_entered, shares)
        else:
            new_balance = int(own[0]["balance"]) + shares
            db.execute("UPDATE stockbalance SET balance = ? WHERE username = ? AND stock = ?",\
                        new_balance, username, symbol_entered)

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ? AND username = ?",\
                    total, session.get("user_id"), username)

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    usr = db.execute("SELECT username FROM users WHERE id = ?", session.get("user_id"))
    username = usr[0]["username"]

    data = db.execute("SELECT stock, qty, price, opdate, operation FROM stocks\
                       WHERE username = ? ORDER BY opdate DESC", username)

    stocks = []
    if data != []:
        for row in data:
            temp = {}
            stock = lookup(row["stock"])
            temp["name"] = stock["name"]
            temp["symbol"] = row["stock"]
            temp["shares"] = row["qty"]
            temp["price"] = usd(row["price"])
            temp["operationDateTime"] = row["opdate"]
            if row["operation"] == "B":
                temp["operation"] = "Bought"
            else:
                temp["operation"] = "Sold"

            stocks.append(temp)

    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol_entered = request.form.get("symbol")

        if not symbol_entered:
            return apology("must provide Stock symbol", 400)

        stock = lookup(symbol_entered)

        if stock == None:
            return apology("Stock symbol not found", 400)

        name = stock['name']
        price = stock['price']
        symbol = stock['symbol']

        price = usd(price)

        return render_template("quoted.html", name=name, price=price, symbol=symbol)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username", 400)

        usr = db.execute("SELECT username FROM users WHERE username = ?", username)
        if usr != []:
            usr_db = usr[0]["username"]
            if usr_db:
                return apology("username already exists. Enter a different username", 400)

        if not password:
            return apology("must provide password", 400)

        if not confirmation:
            return apology("must provide confirmation of password", 400)

        if password != confirmation:
            return apology("Password and its confirmation must be the same", 400)

        hash_pwd = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users(username, hash) VALUES(?,?)", username, hash_pwd)
            return render_template("login.html")
        except:
            return apology("Username already exists in the system.", 400)
    else:
        return render_template("register.html")


@app.route("/changepassword", methods=["GET", "POST"])
def changepassword():
    """Change Password"""
    if request.method == "POST":
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not password:
            return apology("must provide password", 400)

        if not confirmation:
            return apology("must provide confirmation of password", 400)

        if password != confirmation:
            return apology("Password and its confirmation must be the same", 400)

        hash_pwd = generate_password_hash(password)

        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash_pwd, session.get("user_id"))
        return redirect("/")
    else:
        return render_template("changepassword.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        data = db.execute("SELECT username FROM users WHERE id = ?", session.get("user_id"))
        username = data[0]["username"]

        symbol_entered = request.form.get("symbol")
        shares_entered = request.form.get("shares")

        if not symbol_entered:
            return apology("must select Stock symbol", 400)

        stock = lookup(symbol_entered)

        if stock == None:
            return apology("Stock symbol not found", 400)

        price = float(stock["price"])

        if not shares_entered:
            return apology("must provide a number of shares to buy", 400)

        pattern = r'^[1-9]\d*$'
        if not re.search(pattern, shares_entered):
            return apology("Number of shares must by a positive integer", 400)

        shares = int(shares_entered)

        shares_owned = db.execute("SELECT balance FROM stockbalance WHERE balance > 0 AND username = ? \
                          AND stock = ?", username, symbol_entered)

        if shares_owned != []:
            balance = shares_owned[0]["balance"]

            if shares > balance:
                return apology(f"Insufficient numbers of shares of {symbol_entered} to sell: {balance} shares available", 400)

            new_balance = balance - shares
            total = shares * price
        else:
            return apology(f"You don't own shares for {symbol_entered} stock", 400)

        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        formatted_time = now.strftime("%H:%M:%S")
        date_time = formatted_date + " " + formatted_time

        db.execute("INSERT INTO stocks (username, stock, opdate, qty, price, operation) VALUES (?,?,?,?,?,?)",\
                    username, symbol_entered, date_time, shares, price, 'S')

        db.execute("UPDATE stockbalance SET balance = ? WHERE username = ? AND stock = ?",\
                        new_balance, username, symbol_entered)

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ? AND username = ?",\
                    total, session.get("user_id"), username)

        return redirect("/")
    else:
        data = db.execute("SELECT username FROM users WHERE id = ?", session.get("user_id"))
        username = data[0]["username"]

        data = db.execute("SELECT DISTINCT stock FROM stockbalance WHERE balance > 0 AND username = ?", username)
        if data == []:
            return apology("You don't have stocks in your portfolio", 400)

        options = []
        for row in data:
            options.append(row["stock"])

        return render_template("sell.html", options=options)
