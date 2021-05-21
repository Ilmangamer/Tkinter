import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
import os
from tkinter.ttk import *
from tkinter import TclError, messagebox
from logging import exception
import json


# First Window
pim = tk.Tk()
pim.title('HELO WORLD')
pim.geometry('1000x900')

# Image display
load = Image.open("C:/Most used/G&D/Discord1/miniApp-pic.jfif")
imagetkP = ImageTk.PhotoImage(load)
img = ttk.Label(pim, image=imagetkP)
img.Image = imagetkP
img.place(x=0, y=0)


# Entry's
# register here

regL = ttk.Label(pim, text= 'Register here', foreground='white', background='#253873', font=(30))
regL.place(x=365, y=5)

def two_trans():
    #transparency for register window
    pim.configure(bg='#253873')
    pim.wm_attributes("-transparentcolor", "#253873")
    # Transparency for side window
    pim.configure(bg= 'purple')
    pim.wm_attributes("-transparentcolor", 'purple' )

two_trans()

#firstname entry and label
firstnameE = ttk.Entry(pim, background='white', justify='left', font=(45))
firstnameE.place(x= 490, y=65, width=250, height= 35)
    
lEy1 = ttk.Label(pim, text= 'firstname', background='#243E82', foreground='white', justify='left', font=('Times New Roman', 20))
lEy1.place(x= 365, y=65)

#lastname entry and label
lastnameE = ttk.Entry(pim, background='white', justify='left', font=(25))
lastnameE.place(x= 490, y=125, width=250, height= 35)

lastnameL = ttk.Label(pim, text= 'lastname', background='#364799', foreground='white', justify='left', font=('Times New Roman', 20))
lastnameL.place(x= 365, y=125)

# age label and Entry
ageS = Spinbox(pim, from_=12, to_=100, state='readonly')
ageS.place(x= 490, y=185, width=200, height= 29)

ageL = Label(pim, text= 'age', background= '#3855A5', foreground='white', font=('Times New Roman', 19))
ageL.place(x=365, y=185)

# email label and entry
email = ttk.Label(pim, text= 'email', background='#415AA8', foreground='white', font=('Times New Roman', 20))
email.place(x=365, y=245)

emailE= ttk.Entry(pim, text='email', background='white', font=(25))
emailE.place(x=490, y=245, width=260, height= 35)

# username
usrl = ttk.Label(pim, text='username', foreground='white', background='#576BBE', font=('Times New Roman', 20))
usrl.place(x=365, y=305)

usrE= ttk.Entry(pim, background='white', font=(25))
usrE.place(x=490, y=305, width=250, height=35)


# password
passl = ttk.Label(pim, text='password', foreground='white', background='#6674B7', font=('Times New Roman', 20))
passl.place(x=365, y=365)

passE= ttk.Entry(pim, background='white', font=(20))
passE.place(x=490, y=365, width=250, height= 35)

# retype password
passl = ttk.Label(pim, text='Retype password', foreground='white', background='#8988C2', font=('Times New Roman', 14))
passl.place(x=352, y=425)

repassE= ttk.Entry(pim, background='white', font=(20))
repassE.place(x=490, y=425, width=250, height= 35)


# iterating to database
filenameReg = "C:\VS Code\Python\Sublime\Tkinter\DbTOSv.json"
def view_data():
    with open(filenameReg, "r") as f:
        load_Data_Reg = json.load(f)
        for i in load_Data_Reg:
            try:
                firstnameE = i["firstname"]
                lastnameE = i["lastname"]
                ageS = i["age"]
                emailE = i["email"]
                usrE = i["Username"]
                passE = i["password"]
                repassE = i["retyped-password"]
                f.close()
            except KeyError as k:
                print("dear keyerror, there really is no keyerror")
            

# appending to json data
item_Data_Reg = {}
def append_data():
    with open(filenameReg, "r") as file:
        load_Data_Reg = json.load(file)
        item_Data_Reg["firstname"] = firstnameE.get()
        item_Data_Reg["lastname"] = lastnameE.get()
        item_Data_Reg["age"] = ageS.get()
        item_Data_Reg["email"] = emailE.get()
        item_Data_Reg["Username"] = usrE.get()
        item_Data_Reg["password"] = passE.get()
        item_Data_Reg["retyped-password"] = repassE.get()
        load_Data_Reg.append(item_Data_Reg)
        file.close()
        
        with open(filenameReg, "w") as file:
                 json.dump(load_Data_Reg, file, indent = 4)
                 firstnameE.delete(0, 'end')
                 lastnameE.delete(0, 'end')
                 ageS.delete(0, 'end')
                 emailE.delete(0, 'end')
                 usrE.delete(0, 'end')
                 passE.delete(0, 'end')
                 repassE.delete(0, 'end')
                 file.close()

             

# Error if submitting when empty entries
def emptyEy1():
        warning_message = ""
        for widget in [firstnameE, lastnameE, ageS, usrE, passE, repassE]:
                if len(widget.get()) == 0:
                        warning_message = "Please enter credentials"
                print(warning_message, bool(warning_message))
                break
        if not warning_message and (passE.get()) != (repassE.get()):
                warning_message = "Please enter matching passwords"
        if warning_message:
                messagebox.showwarning(title="Warning", message=warning_message)
        else:
            valid_or_not()

# Submit Button
# collecting data when hitting submit
# Two func to the submit button 

def credentials():
    global creds
    creds['text'] = 'Your credentials is saved and stored in a database'

creds = ttk.Label(pim, text = "", background = '#6974C1',  font=('Times New Roman', 15))
#pim.wm_attributes("-transparentcolor", '#6974C1' )
creds.place(x = 400, y= 600)

# A button for closing
su = ttk.Button(pim, text='Exit', command=pim.destroy)
su.place(x=650, y=550)

# emailaddresses for email entry
is_email_valid = False
item = ('@hotmail.com', '@hotmail.co.uk', '@hotmail.fr', '@yahoo.com', '@gmail.com', '@outlook.com', '@msn.com', '@aol.com', '@yahoo.fr', '@yahoo.co.uk', '@yahoo.in', '@yahoo.com.au', '@yahoo.ca') # you forgot the ".com" at the end
# email = emailE.get() - i moved this line to inside the function, emailE.get's value is blank before the the main program starts, you need to check its value for each time the button is pressed

def valid_or_not():
    email = emailE.get() # this way it checks the value EACH time i click the button, not just once and never again
    if email.endswith(item): # this method only takes a string or tuple, you would want to use a tuple as the items variable as i did in line 2 or convert it to tuple before passing
        is_email_valid = True
        append_data(), credentials()
    else:
        messagebox.showinfo(title="email", message="Please enter a valid emailaddress")
    
submitB = ttk.Button(
    pim,
    text ='Confirm',
    command=emptyEy1 
    
    
)
submitB.place(x=540, y=550)

# keep it displayed
pim.mainloop()


# Second window

root = tk.Tk()

# describing the window
root.geometry("1000x800") 

# img label
load = Image.open("C:/Most used/G&D/Discord1/miniApp-pic.jfif")
imagetkP = ImageTk.PhotoImage(load)

img = ttk.Label(root, image=imagetkP)
img.image = imagetkP
img.place(x=0, y=0)

# Entry' 1
usernameE = ttk.Entry(root, justify='left', background="white", font=(45))
usernameE.place(x=450, y=200, width=400, height=50)

# Entry' 2
Login_passwordE = ttk.Entry(root, justify='left',background="white",  font=(45))
Login_passwordE.place(x=450, y=300, width=400, height=50)

#Writing the data to a databas
filenameLog = "C:\VS Code\Python\Sublime\Tkinter\DbTOSv.json"
def view_data_Log():
    with open(filenameLog, "r") as f:
        load_Data_Log = json.load(f)
        for i in load_Data_Log:
            try:
                usernameE = i["username"]
                Login_passwordE = i["password"]
            except KeyError:
                print("Item not found")
            f.close()


#placement = filenameLog
#placement_read= placement.read()
#placement_load = json.loads(load)
#print(placement_load['MyLoginJson']['Username'])
 
item_Data_Log = {}
load_Data_Log = json.load(open(filenameLog))
def append_data_in_Log(load_Data_Log=load_Data_Log):
    with open(filenameLog, "r") as file:
        try:
             item_Data_Log["username"] = usernameE.get()
             item_Data_Log["password"] = Login_passwordE.get()
        except KeyError:
            print("There is no item matching")
        load_Data_Log.append(item_Data_Log)

        
        with open(filenameLog, "w") as fil:
            json.dump(load_Data_Log, fil, indent = 4)
            fil.close()
        
        


def submission_text():
    global aware
    global path
    aware['text'] = 'Your credentials is saved and stored in a database'

aware = ttk.Label(root, text = "", background = '#6974C1',  font=('Times New Roman', 15))
#root.wm_attributes("-transparentcolor", '#6974C1' )
aware.place(x = 300, y= 385)

# Check note
"""
1- get contents of username field x
2- loop over the database looking for that username x
3- if the username is not in the database show an error, else advance to step 4 x
4- get the contents of the password field, then look for the password assigned to the username mentioned before x
5- if the password doesnt matches the one assigned to the username show an error, else advance to step 6 x
6- finally grant access to the user x
"""


mmx,mmy = None,None
def Nodata():
    global mmx,mmy
    mmx,mmy = usernameE.get(),Login_passwordE.get()
    if len(usernameE.get()) and len(Login_passwordE.get())== 0:
        Passcred = messagebox.showerror(title="Error", message="Please enter credentials")

    elif len(usernameE.get()) == 0:
        Passcred = messagebox.showerror(title="Error", message="Please enter credentials")
        
    elif len(Login_passwordE.get()) == 0:
        Passcred = messagebox.showerror(title="Error", message="Please enter credentials")
    
    else:
         view_data_Log()
         print("success")


def Save_Or_ShowPrompt(load_Data_Log = load_Data_Log):
    global mmx,mmy
    item_Data_Reg["Username"]=mmx
    item_Data_Reg["password"]=mmy
    try:
        if item_Data_Reg["Username"] not in [n["Username"] for n in load_Data_Log if len(n) > 2]:
            messagebox.showwarning(title= 'Error', message = "Username not found")
            
        elif item_Data_Reg["password"] != [n["password"] for n in load_Data_Log if len(n) > 2 and n["Username"] == item_Data_Reg["Username"]][0]:
            messagebox.showerror(title="ERROR", message= "Password doesn't match with your profile")
        else:
                print("Access granted")
                usernameE.delete(0, "end")
                Login_passwordE.delete(0, "end")
    except KeyError as k:
        print("Dodge keyerror")

    
# A part of the global statement
path = ttk.Label(root, text = "", background ='#323550', font = ('Times New Roman', 15))
root.wm_attributes("-transparentcolor", '#323550' )
path.place(x = 870, y= 395)

# A func to the submit button

# Submit button
# collecting data when hitting sub
sub = ttk.Button(
    root,
    text ='Submit',
    command= lambda: (
        Nodata(),
        append_data_in_Log(),
        Save_Or_ShowPrompt(load_Data_Log = load_Data_Log)
        
    )
)
sub.place(x=450, y=355, width=75, height = 22)

# user - Label
usr = ttk.Label(root, text ='username', background = '#3855A5', foreground = 'white', font=('Times New Roman', 25))
usr.place(x=300, y= 200)

root.configure(bg ='#3855A5' )
root.wm_attributes("-transparentcolor", '#3855A5' )

# pasword - Label
psw = ttk.Label(root, text ='password', background = '#576BBE', foreground = 'white', font = ('Times New Roman', 25))
psw.place(x=300, y= 300)

# side win
root.configure(bg= 'red')
root.wm_attributes("-transparentcolor", 'red' )

# whole win
root.attributes("-alpha", 0.85)

# Welcome title -label
wl = ttk.Label(root, text = ('Welcome to Mountain'), background ='#2C478F', foreground = 'white', font = ('Times New Roman', 35))
wl.place(x = 300, y = 90 )

# Login -Label
wl = ttk.Label(root, text = (' Login system'), background ='#213877', foreground = 'white', font = ('Times New Roman', 35))
wl.place(x = 728, y = 90 )

####-------
# 'Please prompt ur creds' - title	
pl = tk.Label(root, text= 'Please prompt your credentials down below', background = '#3855A5', foreground = 'white', font=('Times New Roman', 17))
pl.place(x=300, y=150)

# updating the root
root.update()
print(root.winfo_width(), root.winfo_height(), root.winfo_geometry())

root.mainloop()
