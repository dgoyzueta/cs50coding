# Quick AnaLysis of NASDAQ stocks: Closing price versus Yearly Average Price
#### Video Demo:  https://youtu.be/YQZo6VWP6oc
#### Description:
The purpose of the program is to providad a quick analysis of the change in value of the latest price of
a stock from NASDAQ and compare it to its average price taken from the last 12 months.
Requirements: It is necessary to install the library "yfinance" based on Yahoo Finance data on stocks.
The idea is to provide and additional element of thinking to determine if the stocks has lost or gain value
and help in any decision to buy or sell that stock. It is important to keep mind that this does not constitute
a professional advice for financial transaction, just a point of reference, that together with other metrics,
may help in investment decisions.

The program consists of three additional functions apart from the main function.

Purpose of main():
The main program asks the user to input a NASDAQ ticker. It accepts a string of letters, uppercase or lowercase,from 1 to 5 characters. This first input evaluation is done by using regular expressions. The program
uses the module "re" for this goal. If the user inputs just <Enter> with no values on the prompt, the program
ends.
For those values that were entered, the program evaluates if it is a valid NASDAQ ticker. If it is not, it
continues asking the user to enter a valid NASDAQ ticker. If the ticker was valid, it proceeds to obtain
its closing price from the previous day, and its average price from the previos year. Then, the program
calculates the change in value using the formula ((closing price / average price) - 1) * 100. The program
finally evaluates if the price is overvalued or undervalued compare to its historical average and prints
the assessment to the screen.

Purpose of get_average_price_year():
This function accepts as parameter a NASDAQ ticker that was sent from the main function and evaluates if the
value of the parameter is a valid NASDAQ ticker. The program uses the module yfinance for this job by getting
information from the ticker, resulting in a dictionary object, where the program evaluates if the stock belongs
to NASDAQ by evaluating if the exchange is "NMS". It also compares the paremeter with the value of the ticker
in the dictionary. They should be the same. If there is no information, the function returns None. If it is
valid NASDAQ ticker, the function returns True, otherwise, it returns False.

Purpose of get_closing_price():
This function obtains the closing price of the valid NASDAQ ticker entered by the user. This uses the yfinance
module as well. In this case, the function calls the "history" method to return the price of the previous day.
The object returned by the method is a dataframe. The value of the closing price is returned to the main
function by reading the last row of the dataframe.

Purpose of get_average_price_year():
This functions gets the average price of the valid NASDAQ ticker taken from the last year. This functions uses
the yfinance module as well calling the "history" method where it returns a dataframe having all the prices
within the last year. Then it takes the mean of those prices from the dataframe object and returns this value
to the main function.

PROGRAM RUN:
To run the program it is important to have installed the package yfinance first.
