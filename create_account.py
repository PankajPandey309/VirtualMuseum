import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image
from PIL import *


root = tk.Tk()
root.geometry('500x600')
root.title("Create Account")
root.configure(bg='maroon')



Fullname=StringVar()
Email=StringVar()
var = IntVar()
Username=StringVar()
Password=StringVar()
c=StringVar()
phonenumber= StringVar()


temp=StringVar()
Username=StringVar()
Password=StringVar()
uname=StringVar()
pword=StringVar()
        
def database():
   db = "C:\\sqlite\db\pythonsqlite.db"
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   phone=phonenumber.get()
   uname=Username.get()
   pword=Password.get()
   conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Users (Fullname TEXT,Email TEXT,Username TEXT,Password TEXT,Gender TEXT,country TEXT,PhoneNumber TEXT)')
   cursor.execute('INSERT INTO Users (FullName,Email ,Gender,country,PhoneNumber,Username ,Password) VALUES(?,?,?,?,?,?,?)',(name1,email,gender,country,phone,uname,pword,))
   conn.commit()
   
   
   
   

    


def create_acc():
   label_0 = Label(root, text="Create Account ",bg='coral3',width=20,font=("bold", 20))
   label_0.place(x=90,y=53)


   label_1 = Label(root, text="FullName",bg='coral3',width=20,font=("bold", 10))
   label_1.place(x=65,y=130)

   entry_1 = Entry(root,textvar=Fullname,bg='khaki')
   entry_1.place(x=240,y=130)

   label_2 = Label(root, text="Email",bg='coral3',width=20,font=("bold", 10))
   label_2.place(x=65,y=180)

   entry_2 = Entry(root,textvar=Email,bg='khaki')
   entry_2.place(x=240,y=180)

   label_3 = Label(root, text="Gender",bg='coral3',width=20,font=("bold", 10))
   label_3.place(x=65,y=230)

   Radiobutton(root, text="Male",padx = 5,bg='maroon', variable=var, value=1).place(x=235,y=230)
   Radiobutton(root, text="Female",padx = 20,bg='maroon', variable=var, value=2).place(x=290,y=230)
   Radiobutton(root, text="Others",padx = 40,bg='maroon', variable=var, value=3).place(x=370,y=230)

   label_4 = Label(root, text="Country",bg='coral3',width=20,font=("bold", 10))
   label_4.place(x=65,y=280)

   list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

   droplist=OptionMenu(root,c, *list1)
   droplist.config(bg='coral3',width=15)
   c.set('select your country') 
   droplist.place(x=240,y=280)

   label_4 = Label(root, text="Phone Number",bg='coral3',width=20,font=("bold", 10))
   label_4.place(x=65,y=330)

   entry_4 = Entry(root,textvar=phonenumber,bg='khaki')
   entry_4.place(x=240,y=330)

   label_5 = Label(root, text="Username",bg='coral3',width=20,font=("bold", 10))
   label_5.place(x=65,y=380)

   entry_5 = Entry(root,textvar=Username,bg='khaki')
   entry_5.place(x=240,y=380)

   label_6 = Label(root, text="Password",bg='coral3',width=20,font=("bold", 10))
   label_6.place(x=65,y=430)

   entry_6 = Entry(root,textvar=Password,bg='khaki',show="*")
   entry_6.place(x=240,y=430)


   Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=100,y=520)
   Button(root, text='ALREADY have an account \n LOG IN',width=22,bg='brown',fg='white',font=('bold',12),command=login).place(x=280,y=520)

def login():
   root1 = Tk()
   root1.geometry('500x600')
   root1.title("Login")
   root1.configure(bg='steelblue')
   
   label_0 = Label(root1, text="LOGIN ",bg='cyan',width=20,font=("bold", 20))
   label_0.place(x=90,y=53)

   label_1 = Label(root1, text="Username",bg='turquoise',width=20,font=("bold", 10))
   label_1.place(x=100,y=180)

   entry_1 = Entry(root1,textvar=Username)
   entry_1.place(x=290,y=180)
   uname=Username.get()

   label_2 = Label(root1, text="Password",bg='turquoise',width=20,font=("bold", 10))
   label_2.place(x=100,y=230)

   entry_2 = Entry(root1,textvar=Password,bg='cyan')
   entry_2= Entry(root1,show="*").place(x=290,y=230)
   pword=Password.get()
   Button(root1,text="Login",width=10,bg='turquoise',fg='white',font=("bold", 15), command=try_login).place(x=100,y=320)

def try_login():
   
    print("Trying to login...")
    conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
    with conn:
      cursor=conn.cursor()
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM Users WHERE Username=? AND Password=?",(uname,pword))
    result=cursor.fetchall()
    #if(result[0]==-1):
    if ((result[0]!=-1) and (result[0]!=0)):
    #if count!=0:
         messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
         
    else:
         messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
   

#attempt to login button




create_acc()
root.mainloop()

