import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image
from io import BytesIO
import base64
import numpy as np
import sys
import mainpage_2 as mg
import buildings as bui
import os
#sys.setdefaultencoding("ISO-8859-1")

#C:\Users\PANKAJ\AppData\Local\Programs\Python\Python37-32\Scripts

x=710
y=500
root = tk.Tk()
root.geometry('1000x600')
root.title("Events")

c=StringVar()

def database():
   db = "C:\\sqlite\db\pythonsqlite.db"   
   conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cursor=conn.cursor()
   conn.commit()


#making canvas and scroll
if x==710:
   vscrollbar=tk.Scrollbar(root)
   canvas=Canvas(width=1500,height=5500)
   canvas.config(scrollregion=canvas.bbox("all"))
   vscrollbar.config(command=canvas.yview)
   vscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
   frame=tk.Frame(canvas)
   canvas.pack(side="left",expand=False)
   canvas.create_window((0,0),window=frame,anchor=NW)
   vbar=tk.Scrollbar(root)
   
   canvas.create_rectangle(0,0,1500,2500,fill='lightseagreen')
   #putting image_
   photo1=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\lasertag.png")
   photo1=photo1.subsample(3,3)  
   canvas.create_image(300,110,image=photo1)
   #putting image
   photo2=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\bikemadness.png")
   photo2=photo2.subsample(2,2)
   canvas.create_image(980,110,image=photo2)

   info="""EVENTS"""
   canvas.create_text(650,160,fill="navajowhite",font="Times 16 italic bold",text=info)
   #info
   info="""Velore Institute of Technology,Chennai hosts a variety of events throughout the academic year including technological fests(Technovit)\n, College fest(Vibrance) etc which cover various events ranging from technical workshops on trending technological\n advancements to various recreational events covering music concerts, dance battles, EDM nights etc. \nVIT is also known for its vibrant celebrations of various religious festivals such as Navratri, Onam, Holi and many more.\n These events bring forth the large potential of the many gifted students at VIT who are waiting for an oppurtunity to \nexpress their various gifts.  """
   #display text
   canvas.create_text(650,320,fill="purple",font="Times 16 italic",text=info)
   i=0
   #gallery

   conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cur=conn.cursor()




def extract_picture(cursor, picture_id,y):
    sql = "SELECT pic, name,s_head,f_head,description FROM events WHERE pic_id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, afile,sh,fh,desc = cursor.fetchone()
    ext='.png'
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    canvas.create_text(710,y,fill="purple",font="Times 19 italic bold",text=afile)
    y=y+50
    canvas.create_text(710,y,fill="orange",font="Times 19 italic bold",text=sh)
    y=y+50
    canvas.create_text(710,y,fill="blue",font="Times 19 italic bold",text=fh)
    y=y+50
    canvas.create_text(670,y,fill="navajowhite",font="Times 19 italic bold",text=desc,anchor=NW)

   
    
    return ablob

conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
cur = conn.cursor()
y=250
#filename = extract_picture(cur,2001,y)



y=y+200
filename = extract_picture(cur,2003,y)
photo3=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\motormash.png")
photo3=photo3.subsample(3,3)
canvas.create_image(260,550,image=photo3)
def video():
   os.system(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\racing.mp4")
var = IntVar()
rb1 = Button(root, text= "Play Video",bg='orange', command=video).place(x=500,y=600)

def video():
   os.system(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\techno.mp4")
var = IntVar()
rb1 = Button(root, text= "A sneak peek at Techno_VIT",bg='orange', command=video).place(x=570,y=180)

def video():
   os.system(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\Ganesh.mp4")
var = IntVar()
rb1 = Button(root, text= "Cultural celebration",bg='orange', command=video).place(x=870,y=180)



y=y+300
filename = extract_picture(cur,2004,y)
photo4=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\parle-ji.png")
photo4=photo4.subsample(3,3)
canvas.create_image(260,850,image=photo4)

y=y+300
filename = extract_picture(cur,2005,y)
photo5=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\passtheballon.png")
photo5=photo5.subsample(3,3)
canvas.create_image(260,1150,image=photo5)

y=y+300
filename = extract_picture(cur,2006,y)
photo6=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\pithu.png")
photo6=photo6.subsample(2,6)
canvas.create_image(260,1450,image=photo6)

y=y+250
filename = extract_picture(cur,2008,y)
photo7=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\lasertag.png")
photo7=photo7.subsample(3,3)
canvas.create_image(260,1700,image=photo7)

y=y+300
filename = extract_picture(cur,2009,y)
photo8=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\bikemadness.png")
photo8=photo8.subsample(2,2)
canvas.create_image(260,2000,image=photo8)

y=y+300
filename = extract_picture(cur,2010,y)
photo9=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\navratri.png")
photo9=photo9.subsample(2,2)
canvas.create_image(260,2280,image=photo9)



cur.close()
conn.close() 








root.mainloop()
