from tkinter import *
import subprocess

window = Tk()

window.title("Linux App Search Box")
window.geometry('300x100')

lbl = Label(window, text="Search Application,.")
lbl.grid(column=2, row=3)

txt = Entry(window,width=10)
txt.grid(column=2, row=0)

def clicked():
    lbl.configure(text="Searching,..")
    check()

btn = Button(window, text="Search", command=clicked)
btn.grid(column=3, row=0)

def check():
    if len(txt.get()) == 0:
        lbl.configure(text="Please enter,..")
    else:
        f()

def f():
    try:
        null = open("/dev/null", "w")
        subprocess.Popen(txt.get(), stdout=null, stderr=null)
        res = txt.get() + " application found"
        lbl.configure(text=res)
        null.close()
    except OSError:
        res = txt.get() + " application NOT found"
        lbl.configure(text=res)
window.mainloop()

![image](https://github.com/vpdesai2020/Everyday-Python/blob/master/Linux%20app%20search/ss_LTB.png)
