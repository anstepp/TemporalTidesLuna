from tkinter import *
from tkinter import ttk

class Applet(Tk.frame):
	def __init__(self, master):
		self.pack()

		self.entry_box = Tk.entry()
		self.entry_box.pack()

		self.contents = Tk.StringVar()
		self.contents.set("Sample")
		self.entry_box["textvariable"] = self.contents

		self.entry_box.bind('<Key-Return>', self.print_contents())

	
	def print_contents(self, event):
		box_contents = self.contents.get("1.0", "end")
		print(f"Current Box Contents:{box_contents}")
