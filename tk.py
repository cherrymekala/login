from tkinter import *
from tkinter import messagebox as msg

def ok():
	username=e1.get()
	pwd=e2.get()
	
	if username == "" and password == "" :
		msg.showinfo("","Blank not allowed")
		
	elif username == "admin" and pwd == "@123" :
		msg.showinfo("","Login sucessful")
		root.destroy()
		
	else:
		msg.showinfo("","Incorrect username and password")
root=Tk()
root.title("Login")
root.geometry("300x200")
global e1,e2

Label(root,text="Username").place(x=10,y=10)
Label(root,text="Password").place(x=10,y=40)

e1=Entry(root)
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")

Button(root,text="Login",command=ok,height=3,width=13).place(x=10,y=100)

root.mainloop()
