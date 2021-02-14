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

	def quit(_root):
		_root.destroy()

	def update(_root):
		_root.update()
			

class surface:
	def create(width,height):
		_surface = Canvas()
		return _surface

	def pack(_surface):
		_surface.pack(fill=BOTH,expand=1)

class draw:
	def line(_surface,x,y,a,b):
		try:
			_surface.create_line(x,y,a,b)
		except:
			return "unable to draw line"

	def rect(_surface,x,y,a,b):
		try:
			_surface.create_rectangle(x,y,a,b,fill="#05f")
		except:
			return "unable to draw rect"
