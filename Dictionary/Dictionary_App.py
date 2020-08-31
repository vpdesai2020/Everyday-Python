## Building A Dictionary App Using Python

### Installing PyDictionary
# pip install PyDictionary

from PyDictionary import PyDictionary
from tkinter import Entry,LEFT,Button,Tk,Label

global data

def search(dictionary_entry,results):
    dictionary=PyDictionary()
    try:
        data=dictionary.meaning(dictionary_entry.get())
        data=data['Noun']
        text=''
        
        for data_ in data:
            text=text + '\n\n'+str(data_)
        results.configure(text=text,wraplength=300,justify=LEFT)
    except:
        results.configure(text='Check the Spelling\nCheck your connection', wraplength=300,justify=LEFT )

def ui():
    root=Tk()
    root.title("Dictionary")
    heading=Label(root,text='Dictionary',font=('Times',21))
    dictionary_entry=Entry(root)
    results=Label(root)
    search_button=Button(root,text='Search',command=lambda:search(dictionary_entry,results))
    

    ##GUI
    heading.grid(row=0,columnspan=2)
    dictionary_entry.grid(row=1,column=0)
    search_button.grid(row=1,column=3)
    results.grid(row=2,columnspan=2)
    root.geometry('350x120')
    
    root.mainloop()
    
if __name__ == "__main__":
    ui()