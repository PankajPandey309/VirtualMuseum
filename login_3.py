from tkinter import *
from tkinter import messagebox
import sqlite3
import create_account as ca



root = Tk()
root.geometry('500x600')
root.title("Login")
root.configure(bg='steelblue')

temp=StringVar()
Username=StringVar()
Password=StringVar()
uname=StringVar()
pword=StringVar()

def database():
   db = "C:\\sqlite\db\pythonsqlite.db"
   uname=Username.get()
   pword=Password.getconn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cursor=conn.cursor()
   conn.commit()

def login():
   label_0 = Label(root, text="LOGIN ",bg='cyan',width=20,font=("bold", 20))
   label_0.place(x=90,y=53)

   label_1 = Label(root, text="Username",bg='turquoise',width=20,font=("bold", 10))
   label_1.place(x=100,y=180)

   entry_1 = Entry(root,textvar=Username)
   entry_1.place(x=290,y=180)
   uname=Username.get()

   label_2 = Label(root, text="Password",bg='turquoise',width=20,font=("bold", 10))
   label_2.place(x=100,y=230)

   entry_2 = Entry(root,textvar=Password,bg='cyan')
   entry_2= Entry(root,show="*").place(x=290,y=230)
   pword=Password.get()


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
Button(root,text="Login",width=10,bg='turquoise',fg='white',font=("bold", 15), command=mp).place(x=100,y=320)
#Button(root,text="Create Account",width=15,bg='turquoise',fg='white',font=("bold", 15), command=cr).place(x=300,y=320)
#Button(root,text="Create Account",width=15,bg='turquoise',fg='white',font=("bold", 15), command=create_account.create_acc()).place(x=300,y=320)
#Button(root,text="Create Account",width=15,bg='turquoise',fg='white',font=("bold", 15), command=create_account.create_acc).place(x=300,y=320)
login()
root.mainloop()
