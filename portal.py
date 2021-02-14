import tkinter
from tkinter import *

class display:
	def size(x=300,y=250):
		_root = tkinter.Tk()
		_root.geometry(str(x)+"x"+str(y))
		_root.title("Portal window")
		_root.resizable(False,False)
		
		return _root

	def title(_root,title="Portal window"):
		_root.title(title)

	def resizable(_root,x=True,y=True):
		_root.resizable(x,y)

	def update(_root):
		_root.mainloop()

class surface:
	def create(width,height):
		_surface = Canvas()
		return _surface

	def pack(_surface):
		_surface.pack(fill=None,expand=0)

class draw:
	def line(_surface,x,y,a,b):
		_surface.create_line(x,y,a,b)
