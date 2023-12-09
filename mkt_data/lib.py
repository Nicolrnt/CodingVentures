##
## mkt_data/lib.py
##

# Imports
import yfinance as yf

# Get stock info
def get_stock_info(ticker):
	stock = yf.Ticker(ticker)

	return (stock)
