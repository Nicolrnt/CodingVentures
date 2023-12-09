##
## main.py
##

# Imports
import sys

# Routes
from Yolo.main import yolo_main

# Variables
from config import POLYGON_API_KEY

# Main
def main(flags):
	if (len(flags) == 1):
		print("""USAGE : py main.py [strategy]

[strategy]
--yolo - Yolo strategy""")
		return
	if (flags[1] == '--yolo'):
		yolo_main(POLYGON_API_KEY)

# Launcher
if __name__ == '__main__':
	main(sys.argv)
