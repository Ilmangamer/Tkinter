import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk



root = tk.Tk()
root.geometry("345x380")
string_data = StringVar()
operator = ""


# defing button + parameter
# global var
# assign empty operator with empty operator + converted string+parameter
#StringVar has to be set to the data
# StringVar Holds strings, and the default value of it.

#The theory behind it is what I call string games.
# String games is Addding and manipulating strings to acheive what u want.


def but_clicked(numbers):
        global operator
        operator = operator + str(numbers)
        string_data.set(operator)
        
def but_clear():
    global operator
    operator = ""
    string_data.set(operator)

# to sum it I use to globalise the operator
# because then I can access an empty string and it will be universal for the commands and buttons
# I converted str and eval on empty string then I assigned it to a variable
# I had to convert eval on empty string to do basic calculations.
# then I set the strings value to the variable these_sums which do basic calculations 
def sum():
    global operator
    these_sums = eval(operator)
    string_data.set(these_sums)
    
    
   
    


    


E = Entry(root, font=("arial", 20, "bold"), bg= "dark red", insertwidth=4, textvariable= string_data, bd=30, justify="right", width=19)
E.grid(columnspan=4)

but = Button(root, bd=8, padx=16, fg= "white", bg="black", font=("arial", 20, "bold"), text="7",  command= lambda: but_clicked(7))
but.place(x=20, y=95)

but2 = Button(root, bd=8, padx=16, fg= "White", bg="black", font=("arial", 20, "bold"), text="8", command= lambda: but_clicked(8))
but2.place(x=100, y=95)

but3 = Button(root, bd=8, padx=16, fg= "white", bg="black", font=("arial", 20, "bold"), text="9", command= lambda: but_clicked(9))
but3.place(x=180, y=95)

but4 = Button(root, bd=8, padx=16, fg= "white", bg="black", font=("arial", 20, "bold"), text="*", command= lambda: but_clicked("*"))
but4.place(x=260, y=95)

but5 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="4", command= lambda: but_clicked(4))
but5.place(x=20, y=165)

but6 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="5", command= lambda: but_clicked(5))
but6.place(x=100, y=165)

but7 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="6", command= lambda: but_clicked(6))
but7.place(x=180, y=165)

but8 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="-", command= lambda: but_clicked("-"))
but8.place(x=265, y=165)

but11 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="1", command= lambda: but_clicked(1))
but11.place(x=20, y=235)

but12 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="2", command= lambda: but_clicked(2))
but12.place(x=100, y=235)

but13 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="3", command= lambda: but_clicked(3))
but13.place(x=180, y=235)

but14 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="+", command= lambda: but_clicked("+"))
but14.place(x=260, y=235)

but15 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="/", command= lambda: but_clicked("/"))
but15.place(x=20, y=305)

but15 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="0", command= lambda: but_clicked(0))
but15.place(x=100, y=305)

but16 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="C", command=lambda: but_clear())
but16.place(x=180, y=305)

but5 = Button(root, bd=8, padx=16, fg="white", bg="black", font=("arial", 20, "bold"), text="=", command=lambda: sum())
but5.place(x=255, y=305)

root.configure(background="black")

root.mainloop()