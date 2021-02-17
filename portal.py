from PIL import ImageTk, Image

try:
	import tkinter,sys
	from tkinter import *
except :
	import Tkinter,sys
	from Tkinter import *

class init(object):
	"""docstring for display"""
	def __init__(self):
		self._root = None
		self.is_closed = True

	def size(self, width=400, height=300, x=100 , y=100):
		self.width = width
		self.height = height

		self._root = tkinter.Tk()

		self._root.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y))
		self._root.resizable(False,False)
		self._root.title("portal")

		return self._root

	def title(self,title="portal"):
		self._root.title(title)

	def resizable(x=True,y=True):
		self._root.resizable(x,y)

	def totalquit(self):
		sys.exit()

	def update(self):
		self._root.update()

class space(object):
	def create(_root, width=400,height=300,border_width=0,color="black"):
		surf = Canvas(_root, width, height, bd=border_width, bg=color)
		return surf

	def show(surf):
		surf.pack(fill=None,expand=0)

class draw:
	def line(surf, *argv, color="white"):
		surf.create_line(argv, fill=color)

	def poligon(surf, *argv, color="white", outlinebg=None):
		surf.create_poligon(argv,fill=color,outline=outlinebg)

	def oval(surf, *argv, color="white", outlinebg=None):
		surf.create_oval(argv,fill=color, outline=outlinebg)

	def image(surf, image, x, y,pos=None):
		surf.create_image(x,y,anchor=pos)

	def text(surf, Text="this is text", x, y, pos=None ,color="black" ,Font="Arial"):
		surf.create_text(x,y,anchor=pos,font=Font,text=Text,bg=color)

class image:
	def load(path):
		img = Image.open(str(path))
		image = ImageTk.PhotoImage(img)
		return image

	def resize(img,x,y,antialias=False):
		image = img.resize((x,y), if antialias==True:Image.ANTIALIAS)
		return image

	def crop(img, a,b,c,d):
		image = img.crop((a,b,c,d))
		return image

	def flip(img,x,y):
		if x:
			img = img.transpose(Image.FLIP_LEFT_RIGHT)
		if y:
			img = img.transpose(Image.FLIP_TOP_BOTTOM)
		return img
