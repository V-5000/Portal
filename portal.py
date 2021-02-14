import tkinter
from tkinter import *

class display:
	def setSize(x=300,y=250):
		_root = tkinter.Tk()
		_root.geometry(str(x)+"x"+str(y))
		_root.title("Portal window")
		_root.resizable(False,False)
		
		return _root

	def setTitle(_root,title="Portal window"):
		_root.title(title)

	def setResizable(_root,x=True,y=True):
		_root.resizable(x,y)

	def update(_root):
		_root.mainloop()
