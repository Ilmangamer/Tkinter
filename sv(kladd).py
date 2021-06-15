import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
import os
from tkinter.ttk import *
from tkinter import messagebox

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
# reg here

regL = ttk.Label(pim, text= 'Register here', foreground='white', background='#253873', font=(30))
regL.place(x=365, y=5)

def two_trans():
	#transparency for reg window
	pim.configure(bg='#253873')
	pim.wm_attributes("-transparentcolor", "#253873")
	# Transparency for side window
	pim.configure(bg= 'purple')
	pim.wm_attributes("-transparentcolor", 'purple' )

two_trans()


#firstname entry and label

Ey1 = ttk.Entry(pim, background='white', justify='left', font=(45))
Ey1.place(x= 490, y=65, width=250, height= 35)
	
lEy1 = ttk.Label(pim, text= 'firstname', background='#243E82', foreground='white', justify='left', font=('Times New Roman', 20))
lEy1.place(x= 365, y=65)

#lastname entry and label

lastnameE = ttk.Entry(pim, background='white', justify='left', font=(25))
lastnameE.place(x= 490, y=125, width=250, height= 35)

lastnameL = ttk.Label(pim, text= 'lastname', background='#364799', foreground='white', justify='left', font=('Times New Roman', 20))
lastnameL.place(x= 365, y=125)

# age label and Entry
ageS = Spinbox(pim, from_=12, to_=100)
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



# A button and a Function

def save_Alldata():
	textInEy1 = Ey1.get().strip()
	textInEy2 = lastnameE.get().strip()
	textInEy3 = ageS.get().strip()
	textInEy4 = emailE.get().strip()
	textInEy5 = usrE.get().strip()
	textInEy6 = passE.get().strip()
	textInEy7 = repassE.get().strip()

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
		

		op.write('\n')
		op.write(textInEy7)
		op.close()

		#deleting the entry. 
		Ey1.delete(0, 'end')
		lastnameE.delete(0, 'end')
		ageS.delete(0, 'end')
		emailE.delete(0, 'end')
		usrE.delete(0, 'end')
		passE.delete(0, 'end')
		repassE.delete(0, 'end')

		op.close()





# Error if submitting when empty entries
def emptyEy1():
	if len(Ey1.get())== 0:
		Warning = messagebox.showwarning(title="Warning", message="Please enter credentials")
		Warning.place(x=470, y=65)
	
	if len(lastnameE.get()) == 0:
		WarningEy2 = messagebox.showwarning(title="Warning", message="Please enter credentials")
		WarningEy2.place(x=470, y=65)
	
	if len(ageS.get()) == 0:
		WarningEy2 = messagebox.showwarning(title="Warning", message="Please enter credentials")
		WarningEy2.place(x=470, y=65)
	
	if len(usrE.get()) == 0:
		WarningEy2 = messagebox.showwarning(title="Warning", message="Please enter credentials")
		WarningEy2.place(x=470, y=65)
		
	if len(passE.get()) == 0:
		WarningEy2 = messagebox.showwarning(title="Warning", message="Please enter credentials")
		WarningEy2.place(x=470, y=65)
	
	if len(repassE.get()) == 0:
		WarningEy2 = messagebox.showwarning(title="Warning", message="Please enter credentials")
		WarningEy2.place(x=470, y=65)

	if len(passE.get()) != len(repassE.get()):
		Matchp = messagebox.showwarning(title="Warning", message="Please enter matching passwords")
		Matchp.place(x=470, y=65)
	
	else:
	 save_Alldata(), credentials()



#import re
#def emaildata(is_email_valid):
    #data_for_email = emailE.get()
    #is_email_valid = False # You have not assigne
    #for item in [r'@hotmail.com', r'@yahoo.com', r'@gmail.com', r'@outlook.com']:
        #if re.findall(item, data_for_email):
            #return True
    #if not is_email_valid:
                #messagebox.showinfo(title="email", message="Please enter a valid emailaddress")
    #else:
        #return False


#--- :(
#def is_email_valid(email_string):
    #for suffix in ["@hotmail.com", "@yahoo.com", "@gmail.com", "@outlook.com"]:
        #if email_string.endswith(suffix):
           # return True
    
  #  return False


#email_from_form = emailE.get()
#if not is_email_valid(email_from_form):
	#messagebox.showinfo(title="email", message="please enter a valid email address")
#pim.update()



# Submit Button
# collecting data when hitting su

# A func to the submit button
def credentials():
	global creds
	creds['text'] = 'Your credentials is saved and stored in a database'

creds = ttk.Label(pim, text = "", background = '#6974C1',  font=('Times New Roman', 15))
#pim.wm_attributes("-transparentcolor", '#6974C1' )
creds.place(x = 400, y= 600)

# All visual buttons in tkinter window here

# A button for closing
su = ttk.Button(pim, text='Exit', command=pim.destroy)
su.place(x=650, y=550)

# emailaddresses for email entry
is_email_valid = False
item = ('@hotmail', '@hotmail', '@yahoo', '@gmail', '@outlook')
email = emailE.get()

def valid_or_not():
    if email.endswith(item): # this method only takes a string or tuple, you would want to use a tuple as the items variable as i did in line 2 or convert it to tuple before passing
        is_email_valid = True
        save_Alldata(), credentials()
    else:
        tk.messagebox.showinfo(title="email", message="Please enter a valid emailaddress")
        
    
submitB = ttk.Button(
    pim,
    text ='Confirm',
    command= lambda: (
        valid_or_not()
    )
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
bean = ttk.Entry(root, justify='left', background="white", font=(45))
bean.place(x=450, y=200, width=400, height=50)

# Entry' 2
Sv = ttk.Entry(root, justify='left',background="white", show="*", font=(45))
Sv.place(x=450, y=300, width=400, height=50)


# Saving data
def save_data():
	all_text = Sv.get().strip()
	every = bean.get().strip()
	
	#Writing the data to a txt file
	if every:
		op = open('futuredatabase.txt', 'a+')
	
		op.write('\n')
		op.write(every )
		op.write('\n')

		op.write('\n')
		op.write(all_text )
		op.close()
		#clearing the entry
		bean.delete(0, 'end')
		Sv.delete(0, 'end')
		op.close()

def Nodata():
	if len(bean.get()) == 0:
		Passcred = messagebox.showerror(title="Error", message="Please enter credentials")
		Passcred.place(x=470, y=65)
		
	if len(Sv.get()) == 0:
		Passcred = messagebox.showerror(title="Error", message="Please enter credentials")
		Passcred.place(x=470, y=65)
	else:
		mit(), save_data()

# A part of the global statement
path = ttk.Label(root, text = "", background ='#323550', font = ('Times New Roman', 15))
root.wm_attributes("-transparentcolor", '#323550' )
path.place(x = 870, y= 395)

# A func to the submit button

def mit():
	global aware
	global path
	aware['text'] = 'Your credentials is saved and stored in a database'

aware = ttk.Label(root, text = "", background = '#6974C1',  font=('Times New Roman', 15))
#root.wm_attributes("-transparentcolor", '#6974C1' )
aware.place(x = 300, y= 385)

# Submit button
# collecting data when hitting sub
sub = ttk.Button(
	root,
	text ='Submit',
	command= lambda: (
		Nodata()
		
	)
)
sub.place(x=450, y=355, width=75, height = 22)

# user
usr = ttk.Label(root, text ='username', background = '#3855A5', foreground = 'white', font=('Times New Roman', 25))
usr.place(x=300, y= 200)

root.configure(bg ='#3855A5' )
root.wm_attributes("-transparentcolor", '#3855A5' )

# pasword
psw = ttk.Label(root, text ='password', background = '#576BBE', foreground = 'white', font = ('Times New Roman', 25))
psw.place(x=300, y= 300)

# side win
root.configure(bg= 'red')
root.wm_attributes("-transparentcolor", 'red' )

# whole win
root.attributes("-alpha", 0.85)

# Welcome title
wl = ttk.Label(root, text = ('Welcome to Mountain'), background ='#2C478F', foreground = 'white', font = ('Times New Roman', 35))
wl.place(x = 300, y = 90 )

# Login 
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

"""       
okay, in the first one, the second if statement is part of the for loop's block. so it potentially can get run every round of the loop (so 4 times in total). and it is also a part of the first if statement's block, so it only gets run if the re.findall part is true.

the second one is still a part of the for loop, but it is not a part of the first if statement. so it gets run 4 times, regardless of the result of the findall check

the third one is outside the for loop entirely. it only gets run once.
so which one do you think is correct, in this case?
remembering that just prior to the for loop is the line is_email_valid = False 

"""

""" First one
 for item in [r'@hotmail.com', r'@yahoo.com', r'@gmail.com', r'@outlook.com']:
        if re.findall(item, data_for_email):
            is_email_valid = True
            if not is_email_valid:
                messagebox.showinfo(title="email", message="Please enter a valid emailaddress")
"""


""" Second one
   for item in [r'@hotmail.com', r'@yahoo.com', r'@gmail.com', r'@outlook.com']:
        if re.findall(item, data_for_email):
            is_email_valid = True
        if not is_email_valid:
            messagebox.showinfo(title="email", message="Please enter a valid emailaddress")
"""



""" Third one
   for item in [r'@hotmail.com', r'@yahoo.com', r'@gmail.com', r'@outlook.com']:
        if re.findall(item, data_for_email):
            is_email_valid = True
    if not is_email_valid:
        messagebox.showinfo(title="email", message="Please enter a valid emailaddress")

"""