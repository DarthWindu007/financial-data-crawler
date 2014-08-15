try:
	from tkinter import *
except:
	raise ImportError("Please install tkinter module for python3")
from extractdata import *
from stock import *
from headlines import *
import calendar
import matplotlib
matplotlib.use('TkAgg')
from numpy import *
import matplotlib.dates as mdates
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import sys
from ttkcalendar import *


class App(object):
	"""
	This is where most of the GUI happens. We can pass the data
	manually as parameters into the contructor or we can have a
	seperate class just for the data... Dunno what we'll do yet.
	"""
	def __init__(self, master):
		# self.data = data
		self.master = master
		self.ScreenSizeX = master.winfo_screenwidth()  # Get screen width [pixels]
		self.ScreenSizeY = master.winfo_screenheight() # Get screen height [pixels]
		self.ScreenRatio = 0.75                           # Set the screen ratio for width and height
		self.FrameSizeX  = int(self.ScreenSizeX * self.ScreenRatio)
		self.FrameSizeY  = int(self.ScreenSizeY * self.ScreenRatio)
		self.FramePosX   = (self.ScreenSizeX - self.FrameSizeX)/2 # Find left and up border of window
		self.FramePosY   = (self.ScreenSizeY - self.FrameSizeY)/2

		master.geometry("%sx%s+%s+%s" % (self.FrameSizeX,self.FrameSizeY,
			int(self.FramePosX),int(self.FramePosY)))
		master.title("Financial Data")

		self.frame = Frame(master)
		self.frame.grid(sticky=N+W+S+E)

		self.button_width = 5
		self.button_height = 2

		self.stock_name_var = StringVar()
		self.stock_name_var.set("GOOGL")

		self.user_entry = Entry(self.frame)
		self.user_entry.grid(row=0,column=1,columnspan=3,sticky=W+N+S)
		self.user_entry.insert(0,self.stock_name_var.get())
		self.user_entry.bind('<Return>', lambda event: self.comp_s(self.user_entry.get()))

		self.start_date_entry = Calendar(self.frame)
		self.start_date_entry.grid(row=0,column=2,rowspan=4,sticky=W+E+N)
		
		self.end_date_entry = Calendar(self.frame)
		self.end_date_entry.grid(row=0,column=3,rowspan=4,sticky=W+E+N)
		if 'win' not in sys.platform:
			style = ttk.Style()
			style.theme_use('clam')

		self.str_msg_var = StringVar()
		self.str_msg_var.set(get_info("GOOG"))
		self.msg = Message(self.frame,textvariable=self.str_msg_var,width=800,bg="white")
		self.msg.grid(row=3,column=0,sticky=W+N)

		self.button = Button(self.frame,height=self.button_height,width=self.button_width,
			text="Quit",fg="red",command=self.frame.quit)
		self.button.grid(row=0,column=0,sticky=W+N+S)

		self.comp_s(self.stock_name_var.get())
		self.suggestion()
		# s = get_history(self.stock_name_var.get(), 2014, 1, 1, 2014, 8, 5)
		# fname = "newdoc.csv"
		# f = open(fname,"w+")
		# f.write(s)
		# f.close()
		# self.data = extract_data(fname)


		# figure1 = Figure(figsize=(6,4),dpi=100)
		# figure1a = figure1.add_subplot(111)
		# test_x = arange(0.0,3.0,0.01)
		# test_y = sin(2*pi*test_x)
		# x = list(map(mdates.strpdate2num("%m/%d/%Y"),map(lambda x: x[0],self.data[1:])))
		# y = list(map(lambda x: x[-1],self.data[1:]))
		# x = x[::-1]
		# y = y[::-1]
		# figure1a.plot_date(x,y,"b-")
		# figure1.autofmt_xdate(bottom=0.2, rotation=30, ha='right')
		# # figure1a.title(str(data[0][-1]))
		# # figure1a.xlabel("Date")
		# # figure1a.ylabel(str(data[0][-1]))
		
		# dataPlot = FigureCanvasTkAgg(figure1, master=self.frame)
		# dataPlot.show()
		# dataPlot.get_tk_widget().grid(row=1,column=0,columnspan=2,sticky=W+N+S)



		# print(self.start_date_entry.selection)


		
		# self.button = Button(self.frame,height=self.button_height,width=self.button_width,
		# 	text="Submit",bg="blue",command=self.get_info(self.user_entry.get()))
		# self.button.grid(row=0,column=2)

		# Label(self.frame,text="Enter Amount: ").grid(row=4,column=2)
	# def get_inform(self,cname):
	# 	s = get_history(self.user_entry.get(), 2014, 1, 1, 2014, 8, 5)
	# 	fname = "newdoc.csv"
	# 	f = open(fname,"w+")
	# 	f.write(s)
	# 	f.close()
	# 	self.data = extract_data(fname)
	def suggestion(self):
		self.score = get_score(self.stock_name_var.get())
		# print(self.score)
		if self.score >= 0.05:
			self.buy_label = Label(self.frame,text="BUY!",bg="dark green",fg="light green",height=self.button_height,width=self.button_width)
			self.buy_label.grid(row=1,column=2,sticky=W)
		elif self.score <= -0.05:
			self.sell_label = Label(self.frame,text="SELL!",bg="dark red",fg="pink",height=self.button_height,width=self.button_width)
			self.sell_label.grid(row=1,column=2,sticky=W)
		else:
			self.hold_label = Label(self.frame,text="HOLD!",bg="dark blue",fg="light blue",height=self.button_height,width=self.button_width)
			self.hold_label.grid(row=1,column=2,sticky=W)
	
	def comp_s(self,stock_name):
		"""
		Update the Stock information from the User Input
		"""
		self.str_msg_var.set(get_info(stock_name))
		self.stock_name_var.set(stock_name)

		start_d = self.start_date_entry.selection
		end_d = self.end_date_entry.selection
		if start_d == None:
			start_d = calendar.datetime.datetime(2014,1,1)
		if end_d == None:
			end_d = calendar.datetime.datetime.now()

		# print(start_d,end_d)

		s = get_history(self.stock_name_var.get(), start_d.year, start_d.month, start_d.day, end_d.year, end_d.month, end_d.day)
		fname = "newdoc.csv"
		f = open(fname,"w+")
		f.write(s)
		f.close()
		self.data = extract_data(fname)


		figure1 = Figure(figsize=(6,4),dpi=100)
		figure1a = figure1.add_subplot(111)
		test_x = arange(0.0,3.0,0.01)
		test_y = sin(2*pi*test_x)
		x = list(map(mdates.strpdate2num("%m/%d/%Y"),map(lambda x: x[0],self.data[1:])))
		y = list(map(lambda x: x[-1],self.data[1:]))
		x = x[::-1]
		y = y[::-1]
		# print(x)
		figure1a.plot_date(x,y,"b-")
		figure1.autofmt_xdate(bottom=0.2, rotation=30, ha='right')
		dataPlot = FigureCanvasTkAgg(figure1, master=self.frame)
		dataPlot.show()
		dataPlot.get_tk_widget().grid(row=1,column=0,columnspan=2,sticky=W+N+S)
		self.suggestion()
		# print(get_score(self.stock_name_var.get()))
		# pass
if __name__ == '__main__':

	root = Tk()
	app = App(root)
	# print(app.start_date_entry.selection)
	
	root.mainloop()

	# print(get_score("GOOGL"))
	# print(get_score("CSCO"))
	# print(get_score("SIRI"))
	# print(get_score("MSFT"))
	# print(get_score("Dow"))
	# print(get_score("BAC"))
	# print(get_score("JCP"))
	# print(get_score("ORCL"))
	# print(get_score("AMD"))
	# print(get_score("VALE"))
	# print(get_score("AAPL"))
	# print(get_score("S"))
	# print(get_score("KMI"))
	# print(mdates.num2date(735319))
	# print(data)
	# print(s)