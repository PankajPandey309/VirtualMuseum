import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image
from PIL import *


root = tk.Tk()
root.geometry('500x600')
root.title("RESERVATION")
root.configure(bg='violet')


name=StringVar()
idd=StringVar()
car_no=StringVar()
in_time=StringVar()
out_time=StringVar()
slot_id= StringVar()

        
def database():
   db = "C:\\sqlite\db\parking.db"
   name1=name.get()
   id1=idd.get()
   cno=car_no.get()
   it=in_time.get()
   ot=out_time.get()
   st=slot_id.get()
   conn = sqlite3.connect(r"C:\\sqlite\db\parking.db")
   with conn:
      cursor=conn.cursor()
   cursor.execute("INSERT INTO reserves (id, name ,car_no,in_time,out_time,slot_id) VALUES(?,?,?,?,?,?)",(id1,name1,cno,it,ot,st))
   conn.commit()
   
   
   
   


label_0 = Label(root, text="WELCOME TO \n CitiPark ",bg='magenta',width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",bg='coral3',width=20,font=("bold", 10))
label_1.place(x=65,y=130)

entry_1 = Entry(root,textvar=name,bg='khaki')
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Username",bg='coral3',width=20,font=("bold", 10))
label_2.place(x=65,y=180)

entry_2 = Entry(root,textvar=idd,bg='khaki')
entry_2.place(x=240,y=180)

label_4 = Label(root, text="Car Registration Number",bg='coral3',width=20,font=("bold", 10))
label_4.place(x=65,y=240)

entry_4 = Entry(root,textvar=car_no,bg='khaki')
entry_4.place(x=240,y=240)

label_5 = Label(root, text="Parking from:",bg='coral3',width=20,font=("bold", 10))
label_5.place(x=65,y=280)

entry_5 = Entry(root,textvar=in_time,bg='khaki')
entry_5.place(x=240,y=280)

label_6 = Label(root, text="Parking to:",bg='coral3',width=20,font=("bold", 10))
label_6.place(x=65,y=330)

entry_6 = Entry(root,textvar=out_time,bg='khaki')
entry_6.place(x=240,y=330)

label_7 = Label(root, text="Slot no:",bg='coral3',width=20,font=("bold", 10))
label_7.place(x=65,y=380)

entry_7 = Entry(root,textvar=slot_id,bg='khaki')
entry_7.place(x=240,y=380)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=150,y=440)

root.mainloop()

