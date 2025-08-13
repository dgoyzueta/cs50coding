# Stock analysis
#### Video Demo: https://youtu.be/BdMNeM3pf9o
#### Description:

The python program stocks.py does an analysis of a particular stock closing price versus its historical average
price. The program does an assessment of the closing price. If the current price is higher than the historical
average price, it prints on the screen an message "Overvalued". If the current price is lower than its
historical price, then the printed message is "Undervalued". If both prices are the same, the message shown is
"Match". At the end of the message, the program creates a chart where you can see the historical prices of the
stock as a scatter plot, a horizontal line showing the yearly average price, and an "X" showing the current
price at closing.

I particular chose the project to be developed in python only because of my interest in learning more about
the programming language and especifically its use with data analysis which is a particular area I want to
go deeper. For this project, I relied on data coming from Yahoo Finance through the package "yfinance" to get
the stock prices. Also, the program relies on the package "plotext" to create the visualizations of the stock
prices on the Linux terminal. I particulary chose this package because I wanted to produce charts in a Linux
environment and run the program from the command line because I wanted to use the CS50 development
environment for this project.

The program has a main function where it asks the user to provide a stock ticker. If the ticker does not
exists in the data, the program controls for errors and returns an error 404. If the ticker exists, then
it creates a chart, and asks the user to enter new stock ticker again. If the ticker does not have any
data in the dataframe, the program shows an message for that and then ask the user to enter a ticker again.
If the user press just Enter without any value, then the program ends.

This script also have five additional functions as explained below:

Function fetch_stock_data: This function gets the historical data for one year for the ticker that the user
provided. It returns a dataframe to the main function. This data is based on Yahoo Finance information.

Function calculate_average_price: This function calculates the average price from all the dataframe that was
obtained. This is a simple average (not a weighted average) and the idea is to compare this average with
the closing price and provide an assesment of the value of that price.

Function get_current_price: This function gets the price of the previous closing of the stock in the market.
This is not a very current price online from the market but the closing price from the dataframe. Although
it is not an up-to-the-second price, it will give an idea about where the latest closing price of the stock stays
versus its yearly average price. The goal is to give a sense about where the value of stock is, more than
getting an exact price. This is to provide an additional information to assist in investment decisions.

Function determine_valuation: This functions does an assessment of the value of the closing price of the stock
versus its yearly average price. As mentioned above, it produces three values: Undervalued, Overvalued and
Match, dependending on where the closing price is located in relation to the yearly average price. This is
to get a sense about the value of a potential buy or sell and inform the investor.

Function plot_stock_data: This function basically creates a plot on the historical data, the closing price,
and the yearly average price, all together in a single chart. This will give a visual representation of the
numbers, that together with the assessment given by the program, will inform the decision maker when making
investments.

This is short script but useful in providing financial information for a buyer or seller of stocks. It takes
advantage of the libraries "yfinance" and "plotext" to simplify the handling of data for doing calculations
and the plotting of data in an ASCII and Linux environment where GUI features are limited. All this means,
taking advantage of the python programming and its libraries to reduce the amount of code to produce this
kind of analysis and visualizations by considering the environment where the outputs will be shown.
