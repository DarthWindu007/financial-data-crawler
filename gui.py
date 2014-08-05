try:
	from tkinter import *
except:
	raise ImportError("Please install tkinter module for python3")
from extractdata import *
import matplotlib
matplotlib.use('TkAgg')
from numpy import *
import matplotlib.dates as mdates
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import sys


class App(object):
	"""
	This is where most of the GUI happens. We can pass the data
	manually as parameters into the contructor or we can have a
	seperate class just for the data... Dunno what we'll do yet.
	"""
	def __init__(self, master,data):
		self.data = data
		self.master = master
		self.ScreenSizeX = master.winfo_screenwidth()  # Get screen width [pixels]
		self.ScreenSizeY = master.winfo_screenheight() # Get screen height [pixels]
		self.ScreenRatio = 0.5                              # Set the screen ratio for width and height
		self.FrameSizeX  = int(self.ScreenSizeX * self.ScreenRatio)
		self.FrameSizeY  = int(self.ScreenSizeY * self.ScreenRatio*1.5)
		self.FramePosX   = (self.ScreenSizeX - self.FrameSizeX)/2 # Find left and up border of window
		self.FramePosY   = (self.ScreenSizeY - self.FrameSizeY)/2

		master.geometry("%sx%s+%s+%s" % (self.FrameSizeX,self.FrameSizeY,
			int(self.FramePosX),int(self.FramePosY)))
		master.title("Financial Data")

		self.frame = Frame(master)
		self.frame.grid()

		self.button_width = 5
		self.button_height = 2

		figure1 = Figure(figsize=(10,4),dpi=100)
		figure1a = figure1.add_subplot(111)
		test_x = arange(0.0,3.0,0.01)
		test_y = sin(2*pi*test_x)
		x = list(map(mdates.strpdate2num("%m/%d/%Y"),map(lambda x: x[0],data[1:])))
		y = list(map(lambda x: x[-1],data[1:]))
		figure1a.plot_date(x,y,"b-")
		# figure1a.title(str(data[0][-1]))
		# figure1a.xlabel("Date")
		# figure1a.ylabel(str(data[0][-1]))
		
		dataPlot = FigureCanvasTkAgg(figure1, master=master)
		dataPlot.show()
		dataPlot.get_tk_widget().grid(row=1,column=1)

		self.button = Button(self.frame,height=self.button_height,width=self.button_width,
			text="Quit",fg="red",command=self.frame.quit)
		self.button.grid(row=0,column=0)

if __name__ == '__main__':
	data = extract_data("table.csv")
	root = Tk()
	app = App(root,data)
	root.mainloop()

	
	print(data[1])