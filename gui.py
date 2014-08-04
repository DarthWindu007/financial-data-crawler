try:
	from tkinter import *
except:
	raise ImportError("Please install tkinter module for python3")
from extractdata import *

class App(object):
	"""
	This is where most of the GUI happens. We can pass the data
	manually as parameters into the contructor or we can have a
	seperate class just for the data... Dunno what we'll do yet.
	"""
	def __init__(self, master):
		self.master = master
		self.ScreenSizeX = master.winfo_screenwidth()  # Get screen width [pixels]
		self.ScreenSizeY = master.winfo_screenheight() # Get screen height [pixels]
		self.ScreenRatio = 0.3                              # Set the screen ratio for width and height
		self.FrameSizeX  = int(self.ScreenSizeX * self.ScreenRatio)
		self.FrameSizeY  = int(self.ScreenSizeY * self.ScreenRatio*1.5)
		self.FramePosX   = (self.ScreenSizeX - self.FrameSizeX)/2 # Find left and up border of window
		self.FramePosY   = (self.ScreenSizeY - self.FrameSizeY)/2

		master.geometry("%sx%s+%s+%s" % (self.FrameSizeX,self.FrameSizeY,
			int(self.FramePosX),int(self.FramePosY)))

		self.frame = Frame(master)
		self.frame.grid()

		self.button_width = 5
		self.button_height = 2
		
		self.button = Button(self.frame,height=self.button_height,width=self.button_width,
			text="Quit",fg="red",command=self.frame.quit)
		self.button.grid(row=0,column=0)

if __name__ == '__main__':
	root = Tk()
	app = App(root)
	root.mainloop()

	data = extract_data("table.csv")
	print(data[1])