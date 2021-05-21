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


# Writing to database


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

             
    
# append data should be added to the submit button and append data log should be added 
# in nodata
#### ---- here i left of.
        

"""
# A button and a Function
def save_Alldata():
    textInEy1 = Ey1.get().strip()
    textInEy2 = lastnameE.get().strip()
    textInEy3 = ageS.get().strip()
    textInEy4 = emailE.get().strip()
    textInEy5 = usrE.get().strip()
    textInEy6 = passE.get().strip()
    textInEy7 = repassE.get().strip()
"""

"""
    #Writing the data to a txt file
    if textInEy1:
        op = open('futuredatabase.txt', 'a+')	
        op.write('\n')
        op.write(textInEy1)
        op.write('\n')

        op.write('\n')
        op.write(textInEy2)
        
        op.write('\n')
        op.write(textInEy3)
        
        op.write('\n')
        op.write(textInEy4)
        
        op.write('\n')
        op.write(textInEy5)
        
        op.write('\n')
        op.write(textInEy6)
    
       # op.write('\n')
        #op.write(textInEy7)
        op.close()

        # clearing the entry. 
        Ey1.delete(0, 'end')
        lastnameE.delete(0, 'end')
        ageS.delete(0, 'end')
        emailE.delete(0, 'end')
        usrE.delete(0, 'end')
        passE.delete(0, 'end')
        repassE.delete(0, 'end')
        op.close()
"""

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
            usernameE.delete(0, "end")
            Login_passwordE.delete(0, "end")
            fil.close()
        
        

      #  try:
          #  if a == item_data["username"] in append_data():
              #  return True
           # elif a != item_data["username"] in append_data():
               # tk.showwarning(title= 'It is a sin that you tried that', text='Please enter credentials alike the one you created')       
                #file.close()
            #else:
              #  return False
        #except Exception as k:
         #   return False
          #  print("It went something wrong in 'append_data func' ")


def submission_text():
    global aware
    global path
    aware['text'] = 'Your credentials is saved and stored in a database'

aware = ttk.Label(root, text = "", background = '#6974C1',  font=('Times New Roman', 15))
#root.wm_attributes("-transparentcolor", '#6974C1' )
aware.place(x = 300, y= 385)

def Nodata():
    if len(usernameE.get()) and len(Login_passwordE.get())== 0:
        Passcred = messagebox.showerror(title="Error", message="Please enter credentials")

    elif len(usernameE.get()) == 0:
        Passcred = messagebox.showerror(title="Error", message="Please enter credentials")
        
    elif len(Login_passwordE.get()) == 0:
        Passcred = messagebox.showerror(title="Error", message="Please enter credentials")
    
    else:
        submission_text(), view_data_Log()

"""
def NotEqualsUsername():
          Cant_accept = ""
          for widget in item_Data_Log["username"], item_Data_Reg["Username"], item_Data_Log["password"] and item_Data_Reg["password"]:
                if item_Data_Log["username"] != item_Data_Reg["Username"]:
                    not submission_text() and append_data_in_Log()
                    Cant_accept = "Please enter credentials alike the ones you created"
                    print(item_Data_Log["username"], item_Data_Reg["Username"])
                      
                print("Access denied", bool(Cant_accept))
                
                if not Cant_accept and item_Data_Log["password"] != item_Data_Reg["password"]:
                      Cant_accept = "Please enter the password you created"
                break
            
          if Cant_accept:
              messagebox.showerror(title="Error", message= Cant_accept)
                 
          else:
                Save_Or_ShowPrompt()
                return
"""

def Save_Or_ShowPrompt(load_Data_Log = load_Data_Log):
    try:
        if item_Data_Reg["Username"] not in [n["Username"] for n in load_Data_Log[::2]]:
            messagebox.showwarning(tilte= 'Error', message = "Username not found")
            
        elif item_Data_Reg["password"] != [n["password"] for n in load_Data_Log[::2] if n["Username"] == item_Data_Reg["Username"]][0]:
            messagebox.showerror(title="ERROR", message= "Password doesn't match with your profile")
        else:
                print("Access granted")
    except KeyError as k:
        print("Dodge keyerror")
  

"""
1- get contents of username field
2- loop over the database looking for that username
3- if the username is not in the database show an error, else advance to step 4
4- get the contents of the password field, then look for the password assigned to the username mentioned before(i would use a dictionary in the database to store the username-password pairs, the keys would be usernames, and the values would be passwords)
5- if the password doesnt matches the one assigned to the username show an error, else advance to step 6
6- finally grant access to the use
"""

"""
if what_the_user_typed_as_password not in [n["Username"] for n in data]:
    print("No profile with that username intialized")



inp_username = None
while inp_username not in [n["Username"] for n in data] or ...:  #<--- other edge cases
    ...   #<--- ask for other username as input in the entry

def validity_check(username,...):
    if username not in [n["Username"] for n in data] or ...:
        print("Invalid username")
        return
    if password ...:
        print(...)
        return
    ...
    print("successfully logged in!")
    call_some_other_function_to_proceed()


submit_button = Button(...,command=submit(usernameEntry.get(),passwordEntry.get()))

def submit(username,entry):
    if validitycheck(username,entry):
        ... #destroy entries etc. and proceed
    else:
        ... #spit out error and clear entries
"""


"""
item_Data_Reg["Username"] = usernameE.get()
for usernames in item_Data_Reg["Username"]:
    if not usernames in item_Data_Log["username"]:
        tk.messagbox.showwarning(title= "Error", message= "User does not exist")


item_Data_Reg["password"] = passE.get()
for passwords in item_Data_Reg["password"]:
    
"""

    
        
    



#def NotEquealsCre():
   # if every != usrE.get():
    #    ttk.messagebox.showwarning(root, title='Warning', message='Please enter credentials, alike the ones you created')
      #  return False
       # print('False, oh oh it means it exist tclerror')

    
        #print('There might be tclerror among your code')
    ##
      # ttk.messagebox.showwarning(root, tilte='Warning', message='please enter credentials, alike the ones you created.')
    #else:
      #  save_data()
       # return 'valid'

#with open('jsonFile.json', 'r') as f:
 # info = json.read(f)
#user = tkinterEntryUsername.get()
#if tkinterEntryPassword == info['users'][user][password]:
 # do whatever
#------------------------------- here I left of

#lastnameE = ttk.Entry(pim, background='white', justify='left', font=(25))
#lastnameE.place(x= 490, y=125, width=250, height= 35)

#lastnameEinfo = lastnameE.get()

"""
after the user finishes registering you will store a email-password pair(maybe using a dictionary, ex : emails[usr_email] = password)

and when the user tries logging in, first check the email they entered, if the email they entered is one of the registered emails(you can check that using emails.keys()), then try to the if the password matches too, as before the password is the value of the key which is the email, so to access the password we do emails[usr_email] and them compare, ex:
if emails[usr_email] == usrE.get()
this is generally what u need to do, experiment with it if you wanna
and to show warnings if the email/password dont match with the stored ones here's a general to do list:
1- check if the entered email is one of the stored emails, if so proceed to step 2, if not show a warning
2- look in the database and check if the entered password is the password of the entered email(i explained it in the previous message), if so proceed to step 3, if not show a warning
3- finally login the user
i

"""
    
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

#The modes are:

#‘r’ – Python read file. Read mode which is used when the file is only being read
#‘w’ – Python write file. Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
#‘a’ – Python append file. Append mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
#‘r+’ – Special read and write mode, which is used to handle both actions when working with a file
