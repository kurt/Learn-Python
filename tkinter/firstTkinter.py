# Import Module
from tkinter import *
from tkinter import messagebox
# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to Kurt Stewart's UI")
# Set geometry (widthxheight)
root.geometry('350x200')


#adding a label to the root window
lbl = Label(root, text = "Are you a Ready to Rumble?")
lbl.grid()


lbl2 = Label(root, text = "HI?") 
# function to display text when
# button is clicked
def clicked():
    lbl2.configure(text = "I just got clicked")
 
# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

# ----------------------------------------------------------

def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(root, text = "Say Hello", command = hello)
B1.place(x = 0,y = 50)
# ----------------------------------------------------------
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Configure")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is the configuration window").pack()

btn = Button(root,
             text ="Configuration Window",
             command = openNewWindow)
btn.place(x=0, y = 100)
# ---------------------------------------------------------


# all widgets will be here
# Execute Tkinter
root.mainloop()
