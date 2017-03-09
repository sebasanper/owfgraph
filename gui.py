__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'

from Tkinter import *

root = Tk()
root.title = 'First try'

def Button1():
    listbox.insert(END, 'button1 pressed')

def Button2():
    listbox.insert(END, '2nd button pressed')

def Button3():
    text_contents = text.get()
    listbox.insert(END, text_contents)
    text.delete(0, END) # Deletes content of textbox to write another string.

textframe = Frame(root)
listframe = Frame(root)

button1 = Button(textframe, text='Click1', command=Button1)
button2 = Button(textframe, text='Ahora2', command=Button2)
button3 = Button(textframe, text="button3", command=Button3)

text = Entry(textframe)
scrollbar = Scrollbar(listframe, orient=VERTICAL)
listbox = Listbox(listframe, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

button3.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
text.pack(side=LEFT, fill=X, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)

textframe.pack(fill=X)
listframe.pack(fill=BOTH, expand=1)

root.geometry('600x400')

root.mainloop()