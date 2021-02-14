import tkinter
from tkinter import *

class display:
	def __init__(self):
		pass

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

	def getheight(_root):
		return _root.winfo_height()

	def getwidth(_root):
		return _root.winfo_width()

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
	def fill(_surface,color="#000"):
		_surface.create_rectangle(-2,-2,_surface.winfo_width()-1,_surface.winfo_height()-1,fill=color,width=0,outline=color)

	def line(_surface,x,y,a,b,color):
		try:
			_surface.create_line(x,y,a,b,fill=color)
		except:
			return "unable to draw line"

	def rect(_surface,x,y,a,b):
		try:
			_surface.create_rectangle(x,y,a,b,fill="#05f",width=0)
		except:
			return "unable to draw rect"
