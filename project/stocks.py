# Project: Stock analysis
# Name: Daniel Goyzueta Saenz
# GitHub username: dgoyzueta
# Edx account: dgoyzueta
# Location: McLean, VA, US
# Date: 6/13/2025

import yfinance as yf
import plotext as plt

def fetch_stock_data(ticker):
    #Fetch 12 months of daily stock data from Yahoo Finance.
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")
    return data


def calculate_average_price(data):
    #Calculate the average closing price.
    return data['Close'].mean()


def get_current_price(data):
    #Return the latest available closing price.
    return data['Close'].iloc[-1]


def plot_stock_data(data, avg_price, current_price, ticker):
    #Plot stock data with average price and current price.
    #Use of ChatGPT to help create this function.
    dates = data.index.strftime('%d/%m/%Y').tolist()
    prices = data['Close'].tolist()

    last_date = dates[-1]

    plt.clear_data()
    plt.clear_figure()
    plt.title(f"{ticker.upper()} Stock Price - Last 12 Months")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")

    plt.plot(dates, prices, label="Daily Close Prices", color="blue")
    plt.hline(avg_price, color="green")

    plt.scatter([last_date], [current_price], label=f"Current Price: {current_price:.2f} -- Avg Price: {avg_price:.2f}", color="red", marker="X")

    plt.show()
    print()


def determine_valuation(current_price, avg_price):
    #Determine if the stock is overvalued, undervalued, or matches the average.
    if current_price > avg_price:
        return "Overvalued"
    elif current_price < avg_price:
        return "Undervalued"
    else:
        return "Match"


def main():
    while True:
        ticker = input("Enter a NYSE stock ticker (e.g., GOOGL, MSFT) or press Enter to exit: ").strip().upper()

        if ticker == "":
            return

        try:
            data = fetch_stock_data(ticker)
            if data.empty:
                print(f"No data found for the ticker {ticker}")
            else:
                avg_price = calculate_average_price(data)
                current_price = get_current_price(data)

                print()
                print(f"Current Price: ${current_price:.2f}")
                print(f"Average Yearly Price: ${avg_price:.2f}")
                print("Valuation Status:", determine_valuation(current_price, avg_price))
                print()
                plot_stock_data(data, avg_price, current_price, ticker)

        except Exception as e:
            print(f"An error occurred when trying to get information for ticker {ticker}:", str(e))


if __name__ == "__main__":
    main()
