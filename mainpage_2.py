import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image
from PIL import *
import create_account as ca
import os

root = tk.Tk()
root.geometry('1500x600')
root.title("Mainpage")
root.configure(bg='navy')
c=StringVar()

def database():
   db = "C:\\sqlite\db\pythonsqlite.db"
   category=c.get()
   
   conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cursor=conn.cursor()
   conn.commit()


vscrollbar=tk.Scrollbar(root)
canvas2=Canvas(width=1500,height=2500)
canvas2.config(scrollregion=canvas2.bbox("all"))
vscrollbar.config(command=canvas2.yview)
vscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
frame=tk.Frame(canvas2)
canvas2.pack(side="left",expand=False)
canvas2.create_window((0,0),window=frame,anchor=NW)
vbar=tk.Scrollbar(root)

canvas2.create_rectangle(0,0,200,1500,fill='orange')
canvas2.create_rectangle(200,0,2500,1500,fill='palegoldenrod')

def video():
   os.system(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\vit.mp4")
var = IntVar()
rb1 = Button(root, text= "Play Video",bg='yellow', command=video).place(x=10,y=240)


photo1=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\logo.png")
canvas2.create_image(800,120,image=photo1)
#top line
canvas2.create_line(0,0,2000,0,width=60,fill='gold')
canvas2.create_line(0,30,2000,30,width=1,fill='black')
#info
info="""Vellore Institute of Technology is one of the most reputed institutions of academia in the nation.\nWith various fields such as fashion tech, bio tech, MBA, law and engineering under its belt,\n VIT, as an establishment is considered a leading force in the education industry. """
#display text
canvas2.create_text(800,270,fill="darkblue",font="Times 20 italic",text=info)

info="""Chancellor's Welcome!!! """
#display text
canvas2.create_text(800,350,fill="darkblue",font="Times 20 italic bold",text=info)


label_0 = Label(root, text="HOME PAGE ",bg='yellow',width=20,font=("bold", 10))
label_0.place(x=10,y=5)

label_1 = Label(root, text="Username",bg='yellow',width=14,font=("bold", 13))
label_1.place(x=10,y=100)

photo6=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\faculty\ch.png")
canvas2.create_image(800,450,image=photo6)
info="""VIT Chennai Chancellor G. Viswanathan welcomes you to VIT  chennai. """
#display text
canvas2.create_text(660,550,fill="darkblue",font="Times 20 italic",text=info)





info="""Exploring VIT...... """
#display text
canvas2.create_text(800,650,fill="darkblue",font="Times 20 italic bold",text=info)

photo2=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\monument.png")
photo2=photo2.subsample(2,3)
canvas2.create_image(500,820,image=photo2)


photo4=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Shaurya.png")
photo4=photo4.subsample(3,2)
canvas2.create_image(500,1220,image=photo4)

photo5=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\game.png")
canvas2.create_image(1000,820,image=photo5)


photo3=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\art\zayn.png")
photo3=photo3.subsample(3,3)
canvas2.create_image(1000,1220,image=photo3)



Button(root,text="Logout",width=10,bg='yellow',font=("bold", 10)).place(x=10,y=210)
Button(root,text="Events",width=10,bg='yellow',font=("bold", 10)).place(x=10,y=180)
Button(root,text="Buildings",width=10,bg='yellow',font=("bold", 10)).place(x=10,y=150)


root.mainloop()
