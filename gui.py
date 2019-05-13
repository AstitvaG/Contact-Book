from tkinter import *
import time

window = Tk()
window["bg"]="#363636"
window.title("Contacts")
window.geometry("1000x800")
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))

def subm(name,email,mobno,city,pin):
	print(name)	

def add():
	for widget in window.winfo_children():
		widget.destroy()
	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Add Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()
	
	l_name = Label(window,text="Name : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.3,anchor="w")
	name = Entry(window,font=('arial',25),fg="white",bg="#198EB8").place(relx=0.97, rely=0.3, anchor="e")

	l_emailaddr = Label(window,text="Email : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.4,anchor="w")
	email = Entry(window,font=('arial',25),fg="white",bg="#198EB8").place(relx=0.97, rely=0.4, anchor="e")
	
	l_mobno = Label(window,text="Mobile No. : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.5,anchor="w")
	mobno = Entry(window,font=('arial',25),fg="white",bg="#198EB8").place(relx=0.97, rely=0.5, anchor="e")
	
	l_city = Label(window,text="City : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.6,anchor="w")
	city = Entry(window,font=('arial',25),fg="white",bg="#198EB8").place(relx=0.97, rely=0.6, anchor="e")
	
	l_pin = Label(window,text="Pincode : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.7,anchor="w")
	pin = Entry(window,font=('arial',25),fg="white",bg="#198EB8").place(relx=0.97, rely=0.7, anchor="e")
	
	submit = Button(window,text="Submit",bg="#198EB8",fg="white",font=('arial',15),width=7,command=lambda: subm(name.get(),email.get(),mobno.get(),city.get(),pin.get())).place(relx=0.5, rely=0.8, anchor="c")

def lis():
	for widget in window.winfo_children():
		widget.destroy()
	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="List All Contacts",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

def dele():
	for widget in window.winfo_children():
		widget.destroy()
	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Delete a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

def edit():
	for widget in window.winfo_children():
		widget.destroy()
	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Edit a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

def search():
	for widget in window.winfo_children():
		widget.destroy()
	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Search a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

def new():
	for widget in window.winfo_children():
		widget.destroy()
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	button1 = Button(window,text="ADD NEW\nCONTACT",bg="#198EB8",fg="white",font=('arial',15),width=7,command=add).place(relx=.4, rely=.3, anchor="c")
	button2 = Button(window,text="VIEW ALL\nCONTACTS",bg="#198EB8",fg="white",font=('arial',15),width=7,command=lis).place(relx=.6, rely=.3, anchor="c")
	button3 = Button(window,text="DELETE\nCONTACT",bg="#198EB8",fg="white",font=('arial',15),width=7,command=dele).place(relx=.4, rely=.4, anchor="c")
	button4 = Button(window,text="EDIT\nCONTACT",bg="#198EB8",fg="white",font=('arial',15),width=7,command=edit).place(relx=.6, rely=.4, anchor="c")
	button5 = Button(window,text="SEARCH\nCONTACTS",bg="#198EB8",fg="white",font=('arial',15),width=7,command=search).place(relx=.5, rely=.5, anchor="c")

def wec_func():
	for widget in window.winfo_children():
		widget.destroy()
	new()

welc = Label(window,text="WELCOME",bg="#363636",fg="white",font=('arial',32),justify=CENTER).place(relx=.5, rely=.4, anchor="c")
welc_button = Button(window,text="Continue",bg="#198EB8",fg="white",command=wec_func).place(relx=.5, rely=.47, anchor="c")

window.mainloop()