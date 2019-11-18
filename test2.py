from tkinter import *

root = Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=1000, height=1000)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()