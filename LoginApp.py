


import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
import os


root = tk.Tk()


root.geometry("800x600") 

# img label
load = Image.open("C:/Most used/G&D/Discord1/miniApp-pic.jfif")
imagetkP = ImageTk.PhotoImage(load)


img = ttk.Label(root, image=imagetkP)
img.image = imagetkP
img.place(x=0, y=0)

# 'Saving inputed data'
	

#path = ttk.Label(root, text = "", background ='#323550', font = ('Times New Roman', 15))
#root.wm_attributes("-transparentcolor", '#323550' )
#path.place(x = 870, y= 395)



# Entry' 1

bean = ttk.Entry(root, justify='left', background="white", font=(45))
bean.place(x=450, y=200, width=400, height=50)

# Entry' 2
Sv = ttk.Entry(root, justify='left',background="white", show="*", font=(45))
Sv.place(x=450, y=300, width=400, height=50)

# a func for clearing the entry  and saving it
Sv.delete(0, 'end')
def save_dataE1():
	all_text = Sv.get().strip()
	#'checking for empty entry' - stored in txt
	if all_text:
		w = open('Database', 'r+')
		w.write(all_text, '\n')
		w.close()
		w.delete(0, 'end')
	if not os.path.exists('futuredatabase.txt'):
		w = open('futuredatabase.txt' 'w')
		w.write('CredentialsDatabase:\n')
		w.close()


	bean.delete(0, 'end')
def save_data():
	everything = bean.get().strip()
	#checking for empty entry -stored in txt
	if everything:
		w = open('futuredatabase.txt', 'r+')
		w.write(all_text)
		w.close()
		w.delete(0, 'end')
	if not os.path.exists('futuredatabase.txt'):
		w = open('futuredatabase.txt' 'w')
		w.write('CredentialsDatabse:\n')
		w.close()

# Submit button
# A func to the submit button

def mit():
	global aware
	global path
	aware['text'] = 'Your credentials is saved and stored in a database'

aware = ttk.Label(root, text = "", background = '#6974C1', font=('Times New Roman', 15))
root.wm_attributes("-transparentcolor", '#6974C1' )
aware.place(x = 300, y= 385)

# collecting data when hitting sub
sub = ttk.Button(
	root,
	text ='Submit',
	command= lambda: (
		mit(),
		save_data(),
		save_dataE1() 
	)
)

sub.place(x=450, y=355, width=75, height = 22)

# user
usr = ttk.Label(root, text ='username', background = '#3855A5', foreground = 'white', font=('Times New Roman', 25))
usr.place(x=300, y= 200)
root.configure(bg ='#3855A5' )

# pasword
psw = ttk.Label(root, text ='password', background = '#576BBE', foreground = 'white', font = ('Times New Roman', 25))
psw.place(x=300, y= 300)
root.configure(bg= '#576BBE')
root.attributes("-alpha", 0.85)

# Welcome title
wl = ttk.Label(root, text = ('Welcome to Mountain'), background ='#2C478F', foreground = 'white', font = ('Times New Roman', 35))
root.wm_attributes("-transparentcolor", '#576BBE' )
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

#FF 0



 #The argument mode points to a string beginning with one of the following
 #sequences (Additional characters may follow these sequences.):

 #``r''   Open text file for reading.  The stream is positioned at the
         #beginning of the file.

 #``r+''  Open for reading and writing.  The stream is positioned at the
         #beginning of the file.

 #``w''   Truncate file to zero length or create text file for writing.
         #The stream is positioned at the beginning of the file.

 #``w+''  Open for reading and writing.  The file is created if it does not
         #exist, otherwise it is truncated.  The stream is positioned at
         #the beginning of the file.

# ``a''   Open for writing.  The file is created if it does not exist.  The
         #stream is positioned at the end of the file.  Subsequent writes
         #to the file will always end up at the then current end of file,
         #irrespective of any intervening fseek(3) or similar.

 #``a+''  Open for reading and writing.  The file is created if it does not
         #exist.  The stream is positioned at the end of the file.  Subse-
        # quent writes to the file will always end up at the then current
         #end of file, irrespective of any intervening fseek(3) or similar.

         
         	