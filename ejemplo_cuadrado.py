from tkinter import *

master = Tk()

w = Canvas(master, width=250, height=200)
w.create_rectangle(0, 0, 100, 100, fill="black", outline = "white")
#w.create_rectangle(50, 50, 100, 100, fill="red", outline = "blue")
Label(master,text="Geodesi-K", bg= "black", fg="white").place(x=20,y=40)
w.pack()
master.mainloop()