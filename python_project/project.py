#################################################
# Project’s title: Quick AnaLysis of NASDAQ stocks: Closing price versus Yearly Average Price
# Name: Daniel Goyzueta Saenz
# GitHub account: dgoyzueta
# edX username: dgoyzueta
# City and Country: McLean, VA, US
# Date of the video: 05/21/2025
#################################################

import yfinance as yf
import re

# Gets the average price taken for a year for a valid NASDAQ ticker.
def get_average_price_year(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")
    if data.empty:
        return None

    average_price = data["Close"].mean()
    return average_price

# Validates that the input from the user is a valid NASDAQ ticker.
def validate_ticker(ticker):
    pattern = r"^([a-zA-Z]{1,5})?$"

    match = re.search(pattern, ticker)

    if match:
        try:
            web_ticker = yf.Ticker(ticker)
            info = web_ticker.info
            if info:
                return info.get("exchange") == "NMS" and info.get("symbol") == ticker
            else:
                return False
        except Exception:
            return False
    else:
        return False


# Gets the lastest closing price for a valid NASDAQ ticker.
def get_closing_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        return None
    price_at_closing = data['Close'].iloc[-1]
    return price_at_closing


def main():
    while True:
        ticker = input("Enter NASDAQ ticker or just press <Enter> to exit: ").upper().strip()

        if ticker == "":
            return

        if validate_ticker(ticker):
            closing_price = get_closing_price(ticker)
            if closing_price == None:
                print(f"There is no historical information for the ticker {ticker}.")
                return

            average_price_year = get_average_price_year(ticker)
            if average_price_year == None:
                print(f"There is no historical information for the ticker {ticker}.")
                return

            print()
            print("*" * 55)
            print(f"The previous closing price was: ${closing_price:,.2f} per share.")
            print(f"The YEARLY average share price is: ${average_price_year:,.2f}")
            print("*" * 55)

            # Calculates the % change in price between the closing price and the yearly average price.
            change_in_price = ((closing_price / average_price_year) - 1)*100

            # Prints evaluation of the closing price of the ticker.
            if change_in_price == 0:
                print("The closing price is the same as the yearly average price.")
            elif change_in_price < 0:
                print(f"UNDERVALUED. The price is {change_in_price:.2f}% lower than the yearly average price.")
            else:
                print(f"OVERVALUED. The price is {change_in_price:.2f}% higher than the yearly average price.")

            print()
            return
        else:
            print("Invalid NASDAQ ticker. Please try again or just hit <Enter> to exit.")


if __name__ == "__main__":
    main()
