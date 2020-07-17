from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')
def time():
    format=strftime('%H:%M:%S %p')
    lbl.config(text=format)
    lbl.after(1000,time)
lbl=Label(root,font=('Small Fonts',80),background='red',foreground='black')
lbl.pack(anchor='center')
time()
mainloop()