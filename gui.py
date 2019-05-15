from tkinter import *
from tkinter import messagebox
import time
# from PIL import ImageTk,Image
import sqlite3 as sql

window = Tk()
window["bg"]="#363636"
window.title("Contacts")
window.geometry("1000x800")
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
window.resizable(False, False)

def opt(row):
	mess = Tk()
	mess["bg"]="#363636"
	mess.title("Options")
	mess.geometry("500x300")
	mess.resizable(False, False)

	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	
	def edi(row):
		mess.destroy()

		for widget in window.winfo_children():
			widget.destroy()
		namev = StringVar()
		emailv = StringVar()
		mobnov = StringVar()
		cityv = StringVar()
		pinv = StringVar()
		namev.set(row["Name"])
		emailv.set(row["Email"])
		mobnov.set(row["MobNo"])
		cityv.set(row["City"])
		pinv.set(row["Pin"])

		back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
		welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
		heading = Label(window,text="Edit a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

		l_name = Label(window,text="Name : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.3,anchor="w")
		name = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=namev).place(relx=0.97, rely=0.3, anchor="e")

		l_emailaddr = Label(window,text="Email : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.4,anchor="w")
		email = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=emailv).place(relx=0.97, rely=0.4, anchor="e")
		
		l_mobno = Label(window,text="Mobile No. : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.5,anchor="w")
		mobno = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=mobnov).place(relx=0.97, rely=0.5, anchor="e")
		
		l_city = Label(window,text="City : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.6,anchor="w")
		city = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=cityv).place(relx=0.97, rely=0.6, anchor="e")
		
		l_pin = Label(window,text="Pincode : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.7,anchor="w")
		pin = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=pinv).place(relx=0.97, rely=0.7, anchor="e")
		
		def subm():
			cur.execute("DELETE FROM emp WHERE ROWID=?",(row["ROWID"],))
			con.commit()
			try:
				qu1 = namev.get()
				qu2 = emailv.get()
				qu3 = mobnov.get()
				qu4 = cityv.get()
				qu5 = pinv.get()
				with sql.connect("database.db") as conn:
					curr = conn.cursor()
					if(qu1 is "" or qu2 is "" or qu3 is "" or qu4 is ""):
						msg = "One or more empty answers. So no submission."
					else:
						curr.execute("INSERT INTO emp (Name, Email, MobNo, City, Pin) VALUES (?, ?, ?, ?, ?)", (qu1, qu2, qu3, qu4, qu5))
						conn.commit()
						msg = "Record successfully edited"
			except:
				conn.rollback()
				msg = "Error in edit operation"
			finally:
				messagebox.showinfo("Message",msg)
				conn.close()
				lis()
		submit = Button(window,text="Done",bg="#198EB8",fg="white",font=('arial',15),width=7,command=subm).place(relx=0.5, rely=0.8, anchor="c")
	
	def delet(row):
		mess.destroy()
		dt = Tk()
		dt["bg"]="#363636"
		dt.title("Options")
		dt.geometry("500x150")
		dt.resizable(False, False)
		
		def deleteEntry(row):
			cur.execute("DELETE FROM emp WHERE ROWID=?",(row["ROWID"],))
			con.commit()
			dt.destroy()
			lis()

		head = Label(dt,text="Are you sure\nyou want to delete this entry ?",fg="white",font=("arial",20),bg="#363636").pack()
		no = Button(dt,text="No",font=('arial',15),command = lambda: dt.destroy(),width=10,bg="#198EB8").place(relx=0.3, rely=0.7, anchor="c")
		yes = Button(dt,text="Yes",font=('arial',15),command = lambda: deleteEntry(row),width=10,bg="#198EB8").place(relx=0.7, rely=0.7, anchor="c")

	head = Label(mess,text="What do you want to do with this entry:",font=("arial",20),fg="#198EB8",bg="#363636").pack()
	Disp = Label(mess,text="Name: "+row["Name"]+"\nEmail: "+row["Email"]+"\nMobile No: "+row["MobNo"]+"\nCity: "+row["City"]+"\nPincode: "+row["Pin"],font=('arial',15),fg="white",bg="#363636").pack()
	dle = Button(mess,text="Delete",font=('arial',15),command = lambda: delet(row),width=10,bg="#198EB8").place(relx=0.3, rely=0.65, anchor="c")
	edit = Button(mess,text="Edit",font=('arial',15),command = lambda: edi(row),width=10,bg="#198EB8").place(relx=0.7, rely=0.65, anchor="c")
	bck = Button(mess,text="Back",font=('arial',15),command = lambda : mess.destroy(),width=10,bg="#198EB8").place(relx=0.5, rely=0.82, anchor="c")


def add():
	for widget in window.winfo_children():
		widget.destroy()
	namev = StringVar()
	emailv = StringVar()
	mobnov = StringVar()
	cityv = StringVar()
	pinv = StringVar()

	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Add Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()
	
	l_name = Label(window,text="Name : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.3,anchor="w")
	name = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=namev).place(relx=0.97, rely=0.3, anchor="e")

	l_emailaddr = Label(window,text="Email : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.4,anchor="w")
	email = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=emailv).place(relx=0.97, rely=0.4, anchor="e")
	
	l_mobno = Label(window,text="Mobile No. : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.5,anchor="w")
	mobno = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=mobnov).place(relx=0.97, rely=0.5, anchor="e")
	
	l_city = Label(window,text="City : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.6,anchor="w")
	city = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=cityv).place(relx=0.97, rely=0.6, anchor="e")
	
	l_pin = Label(window,text="Pincode : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.7,anchor="w")
	pin = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=pinv).place(relx=0.97, rely=0.7, anchor="e")
	
	def subm():
		try:
			qu1 = namev.get()
			qu2 = emailv.get()
			qu3 = mobnov.get()
			qu4 = cityv.get()
			qu5 = pinv.get()
			with sql.connect("database.db") as con:
				cur = con.cursor()
				if(qu1 is "" or qu2 is "" or qu3 is "" or qu4 is ""):
					msg = "One or more empty answers. So no submission."
				else:
					cur.execute("INSERT INTO emp (Name, Email, MobNo, City, Pin) VALUES (?, ?, ?, ?, ?)", (qu1, qu2, qu3, qu4, qu5))
					con.commit()
					msg = "Record successfully added"
		except:
			con.rollback()
			msg = "Error in insert operation"
		finally:
			messagebox.showinfo("Message",msg)
			con.close()
			new()


	submit = Button(window,text="Submit",bg="#198EB8",fg="white",font=('arial',15),width=7,command=subm).place(relx=0.5, rely=0.8, anchor="c")

def edit():
	for widget in window.winfo_children():
		widget.destroy()
	namev = StringVar()
	emailv = StringVar()
	mobnov = StringVar()
	cityv = StringVar()
	pinv = StringVar()

	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Edit a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

	l_name = Label(window,text="Name : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.3,anchor="w")
	name = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=namev).place(relx=0.97, rely=0.3, anchor="e")

	l_emailaddr = Label(window,text="Email : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.4,anchor="w")
	email = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=emailv).place(relx=0.97, rely=0.4, anchor="e")
	
	l_mobno = Label(window,text="Mobile No. : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.5,anchor="w")
	mobno = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=mobnov).place(relx=0.97, rely=0.5, anchor="e")
	
	l_city = Label(window,text="City : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.6,anchor="w")
	city = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=cityv).place(relx=0.97, rely=0.6, anchor="e")
	
	l_pin = Label(window,text="Pincode : ",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.03, rely=0.7,anchor="w")
	pin = Entry(window,font=('arial',25),fg="white",bg="#198EB8",textvariable=pinv).place(relx=0.97, rely=0.7, anchor="e")
	
	def subm():
		try:
			qu1 = namev.get()
			qu2 = emailv.get()
			qu3 = mobnov.get()
			qu4 = cityv.get()
			qu5 = pinv.get()
			with sql.connect("database.db") as con:
				cur = con.cursor()
				if(qu1 is "" or qu2 is "" or qu3 is "" or qu4 is ""):
					msg = "One or more empty answers. So no submission."
				else:
					cur.execute("INSERT INTO emp (Name, Email, MobNo, City, Pin) VALUES (?, ?, ?, ?, ?)", (qu1, qu2, qu3, qu4, qu5))
					con.commit()
					msg = "Record successfully added"
		except:
			con.rollback()
			msg = "Error in insert operation"
		finally:
			messagebox.showinfo("Message",msg)
			con.close()
			new()


	submit = Button(window,text="Submit",bg="#198EB8",fg="white",font=('arial',15),width=7,command=subm).place(relx=0.5, rely=0.8, anchor="c")


def lis():
	for widget in window.winfo_children():
		widget.destroy()

	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="List All Contacts",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()

	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select ROWID,* from emp")
	rows = cur.fetchall()


	
	if(len(rows)==0):
		heading = Label(window,text="No contacts added yet..",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()
	else:
		optionHead = Button(window,text=">",bg="#198EB8",fg="white",font=('arial',15)).place(relx=0.099, rely=0.2, anchor="c")
		nameHead = Button(window,text="Name",bg="#198EB8",fg="white",font=('arial',15),width=10).place(relx=0.2, rely=0.2, anchor="c")
		emailHead = Button(window,text="Email",bg="#198EB8",fg="white",font=('arial',15),width=18).place(relx=0.275, rely=0.2, anchor="w")
		mobnoHead = Button(window,text="Mobile",bg="#198EB8",fg="white",font=('arial',15),width=10).place(relx=0.513, rely=0.2, anchor="w")
		cityHead = Button(window,text="City",bg="#198EB8",fg="white",font=('arial',15),width=8).place(relx=0.663, rely=0.2, anchor="w")
		pinHead = Button(window,text="Pincode",bg="#198EB8",fg="white",font=('arial',15),width=5).place(relx=0.791, rely=0.2, anchor="w")
		x = 0.2525
		for row in rows:
			o = Button(window,text=">",font=('arial',15),command = lambda : opt(row)).place(relx=0.099, rely=x, anchor="c")
			n = Button(window,text=row["Name"],font=('arial',15),width=10).place(relx=0.2, rely=x, anchor="c")
			e = Button(window,text=row["Email"],font=('arial',15),width=18).place(relx=0.275, rely=x, anchor="w")
			m = Button(window,text=row["MobNo"],font=('arial',15),width=10).place(relx=0.513, rely=x, anchor="w")
			c = Button(window,text=row["City"],font=('arial',15),width=8).place(relx=0.663, rely=x, anchor="w")
			p = Button(window,text=row["Pin"],font=('arial',15),width=5).place(relx=0.791, rely=x, anchor="w")
			x += 0.0525
					

def dele():
	for widget in window.winfo_children():
		widget.destroy()
	back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Delete a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()



def search():
	for widget in window.winfo_children():
		widget.destroy()
	backtoback = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
	welctowelc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	heading = Label(window,text="Search a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()
	heading1 = Label(window,text="Enter details you want to search : ",bg="#363636",fg="white",font=('arial',20),justify=CENTER).place(relx=0.1,rely=0.2,anchor="w")
	
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	sv = StringVar()
	def callback(sv):
		for widget in window.winfo_children():
			widget.destroy()
		back = Button(window,text="Back",bg="#198EB8",fg="white",font=('arial',15),width=7,command=new).place(relx=0.03, rely=0.03)
		welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
		headin = Label(window,text="Search a Contact",bg="#363636",fg="white",font=('arial',25),justify=CENTER).pack()
		headig1 = Label(window,text="Enter details you want to search : ",bg="#363636",fg="white",font=('arial',20),justify=CENTER).place(relx=0.1,rely=0.2,anchor="w")
		
		sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
		e = Entry(window, textvariable=sv,font=('arial',20),width=23).place(relx=0.5,rely=0.2,anchor="w")
		e = Button(window,text="O",width=1,fg="white",bg="#198EB8").place(relx=0.86,rely=0.2,anchor="w")
		
		cur = con.cursor()
		var = sv.get()
		Variable = var.lower()
		cur.execute("SELECT * FROM emp WHERE LOWER(Name||Email||MobNo||City||Pin) like '%'||?||'%'", (Variable,))
		rows = cur.fetchall()
		if(len(rows)==0):
			heading12 = Label(window,text="No contacts of required type found",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.5,rely=0.3,anchor="c")
		elif(Variable ==""):
			heading12 = Label(window,text="Enter a string to search",bg="#363636",fg="white",font=('arial',25),justify=CENTER).place(relx=0.5,rely=0.3,anchor="c")
		else:
			optionHead = Button(window,text=">",bg="#198EB8",fg="white",font=('arial',15)).place(relx=0.099, rely=0.3, anchor="c")
			nameHead = Button(window,text="Name",bg="#198EB8",fg="white",font=('arial',15),width=10).place(relx=0.2, rely=0.3, anchor="c")
			emailHead = Button(window,text="Email",bg="#198EB8",fg="white",font=('arial',15),width=18).place(relx=0.275, rely=0.3, anchor="w")
			mobnoHead = Button(window,text="Mobile",bg="#198EB8",fg="white",font=('arial',15),width=10).place(relx=0.513, rely=0.3, anchor="w")
			cityHead = Button(window,text="City",bg="#198EB8",fg="white",font=('arial',15),width=8).place(relx=0.663, rely=0.3, anchor="w")
			pinHead = Button(window,text="Pincode",bg="#198EB8",fg="white",font=('arial',15),width=5).place(relx=0.791, rely=0.3, anchor="w")
			x = 0.3525
			for row in rows:
				o = Button(window,text=">",font=('arial',15),command = lambda : opt(row)).place(relx=0.099, rely=x, anchor="c")
				n = Button(window,text=row["Name"],font=('arial',15),width=10).place(relx=0.2, rely=x, anchor="c")
				e = Button(window,text=row["Email"],font=('arial',15),width=18).place(relx=0.275, rely=x, anchor="w")
				m = Button(window,text=row["MobNo"],font=('arial',15),width=10).place(relx=0.513, rely=x, anchor="w")
				c = Button(window,text=row["City"],font=('arial',15),width=8).place(relx=0.663, rely=x, anchor="w")
				p = Button(window,text=row["Pin"],font=('arial',15),width=5).place(relx=0.791, rely=x, anchor="w")
				x += 0.0525

	sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
	e = Entry(window, textvariable=sv,font=('arial',20),width=23).place(relx=0.5,rely=0.2,anchor="w")
	e = Button(window,text="O",width=1,fg="white",bg="#198EB8").place(relx=0.86,rely=0.2,anchor="w")

def new():
	for widget in window.winfo_children():
		widget.destroy()
	welc = Label(window,text="CONTACT BOOK",bg="#363636",fg="white",font=('arial',50),justify=CENTER).pack()
	button1 = Button(window,text="ADD NEW\nCONTACT",bg="#198EB8",fg="white",font=('arial',15),width=10,command=add).place(relx=.4, rely=.2, anchor="c")
	button2 = Button(window,text="VIEW ALL\nCONTACTS",bg="#198EB8",fg="white",font=('arial',15),width=10,command=lis).place(relx=.6, rely=.2, anchor="c")
	# button3 = Button(window,text="DELETE\nCONTACT",bg="#198EB8",fg="white",font=('arial',15),width=10,command=dele).place(relx=.4, rely=.3, anchor="c")
	# button4 = Button(window,text="EDIT\nCONTACT",bg="#198EB8",fg="white",font=('arial',15),width=10,command=edit).place(relx=.6, rely=.3, anchor="c")
	button5 = Button(window,text="SEARCH\nCONTACTS",bg="#198EB8",fg="white",font=('arial',15),width=10,command=search).place(relx=.5, rely=.3, anchor="c")
	# canvas = Canvas(window, width = 1000, height = 470, bg="#363636",highlightthickness=0)  
	# canvas.place(relx=0.5,rely=1,anchor="s")  
	# img = ImageTk.PhotoImage(Image.open("main.png"))  
	# canvas.create_image(20, 20, anchor="nw", image=img)
	# canvas.mainloop()


def wec_func():
	for widget in window.winfo_children():
		widget.destroy()
	new()

welc = Label(window,text="WELCOME",bg="#363636",fg="white",font=('arial',32),justify=CENTER).place(relx=.5, rely=.4, anchor="c")
welc_button = Button(window,text="Continue",bg="#198EB8",fg="white",command=wec_func).place(relx=.5, rely=.47, anchor="c")

window.mainloop()