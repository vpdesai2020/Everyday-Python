from tkinter import *
from yahoo_fin import stock_info
import webbrowser

def callback(url):
    webbrowser.open_new(url)
window = Tk()

window.title("Stock Price Search Box")
window.geometry('350x120')

lbl = Label(window, text="Enter company notation/symbol")
lbl.grid(column=2, row=3)

txt = Entry(window,width=20)
txt.grid(column=2, row=2)

link1 = Label(window, text="Find Here", fg="blue", cursor="hand2")
link1.grid(column=3, row=3)
#link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://www.marketwatch.com/tools/quotes/lookup.asp"))

def clicked():
    lbl.configure(text="Searching,..")
    check()

btn = Button(window, text="Search", command=clicked)
btn.grid(column=3, row=2)

def check():
    if len(txt.get()) == 0:
        lbl.configure(text="Please enter,..")
    else:
        f()

def f():
    try:
        price=stock_info.get_live_price(txt.get())
        res = "Current stock price of "+txt.get() + " is :  "
        lbl.configure(text=res)
        stock = Label(window, text=price)
        stock.grid(column=3, row=3)
       
        
    except OSError:
        res = txt.get() + " NOT found"
        lbl.configure(text=res)
window.mainloop()