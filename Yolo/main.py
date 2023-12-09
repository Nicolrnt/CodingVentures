##
## Yolo/main.py
##

# Imports
import requests
from mkt_data.lib import get_stock_info

# Variables
from Yolo.snp500_ticker_list import SNP500_ticker_list

# # Get stock info
# def get_stock_info(POLYGON_API_KEY, ticker):
# 	# url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-01-09/2023-01-09?apiKey=2dwCD1h_00pTq7wNCXQjg9xasQxQZvCC"
# 	# url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-01-09/2023-01-09?apiKey={POLYGON_API_KEY}"
# 	endpoint = "https://api.polygon.io"
# 	route = f"/v1/open-close/{ticker}/2023-12-01"
# 	credential = f"?apiKey={POLYGON_API_KEY}"
# 	url = endpoint + route + credential

# 	print(url)
# 	response = requests.get(url)
# 	print(response)
# 	print(response.text)

# Main
def yolo_main(POLYGON_API_KEY):
	for ticker in SNP500_ticker_list:
		print(ticker)
		stock = get_stock_info(ticker)
		print(stock.info)
		break
