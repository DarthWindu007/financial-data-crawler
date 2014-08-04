try:
	from tkinter import *
except:
	raise ImportError("Please install tkinter module for python3")
from extractdata import *


if __name__ == '__main__':
	data = extract_data("table.csv")
	print(data[1])