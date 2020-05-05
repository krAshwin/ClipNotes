from tkinter import *
import sys
import pyperclip
import datetime
import os

window = Tk()
window.title("Additional Comments")
entry = Entry(window)
entry.grid(row=0,column=0)
entry.focus()
value = ""
def onclick(event=None):
    value = entry.get()
    path = "/root/Desktop/notes.txt"
    f = open(path,"a")
    text = str(datetime.datetime.now())+" : "+value+"\n----------------------------------\n"+str(pyperclip.paste())+"\n\n\n"
    f.write(text)
    f.close()
    sys.exit(1)
window.bind('<Return>',onclick)
btn=Button(window, text="Submit", bg="white", command=onclick)
btn.grid(row=1)
window.mainloop()
