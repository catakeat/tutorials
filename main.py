import tkinter
import os
import threading



class MainWindow(tkinter.Tk):

    def __init__(self,*args,**kwargs):
        tkinter.Tk.__init__(self,*args,**kwargs)
        frame=tkinter.Frame(self,width=args[0],height=args[1])
        frame.grid(row=0,column=0)
        frame.grid_propagate(0)
        self.createMenu1(self)
        but1=tkinter.Button(frame,text="test")
        but1.bind("<Button-1>",self.test)
        but1.grid()



    def createMenu1(self,parent):
        menubar1=tkinter.Menu(parent)
        filemenu1=tkinter.Menu(menubar1,tearoff=0)
        filemenu1.add_command(label="Command1",command=self.test)
        filemenu1.add_command(label="Command2")
        filemenu1.add_command(label="Command3")
        filemenu1.add_separator()
        filemenu1.add_command(label="Command4")
        menubar1.add_cascade(label="File",menu=filemenu1)

        filemenu2 = tkinter.Menu(menubar1, tearoff=0)
        filemenu2.add_command(label="Edit1")
        filemenu2.add_command(label="Edit2")
        filemenu2.add_command(label="Edit3")
        filemenu2.add_separator()
        filemenu2.add_command(label="Edit4")
        menubar1.add_cascade(label="Edit", menu=filemenu2)
        self.config(menu=menubar1)

    def test(self,event=None):
        ping=os.system("Ping "+ "10.36.4.44")
        if ping==0:
            print("Online")
        else:
            print("Offline")

root=MainWindow("1400","600")
#root.test()
root.mainloop()