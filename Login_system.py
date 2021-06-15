
# make the frame tk
# with func, for know train with OOP

# pack is geometry manager that packs around edges of cavity

import tkinter as Tk


# to create the window


#class Main():
	#def __init__(self, tkinter.Tk, fr,):
		#self.main
		#self.tkinter
		#self.fr
		#self.pack

"""Wait with objects, that will come soon."""


main = Tk.Tk()

# to rename title
main.title('Nicia')


#Creating label -- label widgets
fr = Tk.Label(main, bg= None, bd= 8, height = 23, text = "i don't interpreate", font=("Arial Bold", 12))
fr.grid(column = 3, row = 5)

# Creating grid
# Entry

txt = Tk.Entry(main,width = 10)

txt.grid(column = 1, row = 0)

# button widget 





#button widget - Entry
from tkinter import ttk
def clicked():
	iop = "Welcome to my" + txt.get()
	fr.configure(text = iop)
# you will have to configure your text and assing it to your variable.
bt = Tk.Button(main, text='Enter', command=clicked, font=('Times New Roman', 10))
bt = ttk.Entry()
bt.grid(column=2, row=0)
clicked()


# Making a Checkbutton
# Make sure the booleanvar is set to true

chk = Tk.BooleanVar()
chk.set(True)
chk = Tk.Checkbutton(main, text = 'Select', var = chk)
chk.grid(column = 5, row =3)


# Unique value only otherwise error occurs
# Radio button
def rads():
	rad1 = Tk.Radiobutton(main, text ='Python', value = 0)
	rad2 = Tk.Radiobutton(main, text ='Java', value =1)
	rad3 = Tk.Radiobutton(main, text ='Javascript', value = 2)
	rad4 = Tk.Radiobutton(main, text ='None', value = 4)
	rad1.grid(column = 6, row= 7)
	rad2.grid(column = 6, row= 8)
	rad3.grid(column = 6, row= 9)
	rad4.grid(column = 6, row = 10)

rads()


# scrolled text
from tkinter import scrolledtext 
def scr():
	txt = scrolledtext.ScrolledText(main, width = 40, height = 10)
	txt.grid(column = 10, row = 5)

scr()


# messagebox
# you have to actually import the module
from tkinter import messagebox

def message():
	messagebox.showwarning('Warning', 'virus detected')
mansa =Tk.Button(main, text ='Enter', command = message)
mansa.grid(column= 4, row = 2)





def clicked():
	global Button
	btn['text'] = 'You clicked me'


btn = Tk.Button(main, text ='Click me', command= clicked)
btn.grid(column= 9, row =9)


message()




def func():
    global lable
    global button
    lable['text'] = 'clicked!'
    button['text'] = 'changed'


lable = Tk.Label(main, text='helle')
lable.grid(column= 10, row=8)

button = Tk.Button(main, text='Button', command=func)
button.grid(column= 11, row=12)	






# making combo box for this to be able import the module
# current sets the current value +1
from tkinter.ttk import*

combo = Combobox(main)
combo['values'] = (1, 2, 3, 4, 5, 'text')
combo.current(4)
combo.grid(column = 4, row= 3)






# themed tkinter
# kinda like windows 7 in win7 and 10 in win10
# is to upgrade widgets to new user interface




main.geometry("1002x100")


# default screensize. The deafualt screensize numbs can only be in strings.


# Define the event when the button is clicked.
# label event goes for text etc. while button widget goes only for buttons don't mix!!
# Here we need configure because that is the part of the function that will execute	the button click event.







# showing it to the screen	

# The loop is necassary to constantly keep the window displayed.iopy
main.mainloop()



 		

# Frameworks - pack -super - and master
#class App(tk.Frame):
	#def __init__(self, master = None):
		#super().__init__(master)
		#self.pack 

# Creating the applications

#myapp = App()

# methods that call to the window manager class/ eidts your GUI


#myapp.master.title("You, hey was good")
#myapp.master.maxsize(1000, 500)

# to keep it displayed	

#myapp.mainloop()

