import tkinter
from tkinter import *

class display:
	def setSize(x=300,y=250):
		_root = tkinter.Tk()
		_root.geometry(str(x)+"x"+str(y))
		return _root

	def update(_root):
		_root.mainloop()
