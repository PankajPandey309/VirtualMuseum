import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image
from io import BytesIO
import base64
import numpy as np
import sys
import os
#import mainpage_2 as mg
#sys.setdefaultencoding("ISO-8859-1")

#C:\Users\PANKAJ\AppData\Local\Programs\Python\Python37-32\Scripts

x=710
y=500
root = tk.Tk()
root.geometry('1000x600')
root.title("Buildings")

c=StringVar()

def database():
   db = "C:\\sqlite\db\pythonsqlite.db"   
   conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cursor=conn.cursor()
   conn.commit()


#making canvas and scroll
vscrollbar=tk.Scrollbar(root)
canvas=Canvas(width=1500,height=5500)
canvas.config(scrollregion=canvas.bbox("all"))
vscrollbar.config(command=canvas.yview)
vscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
frame=tk.Frame(canvas)
canvas.pack(side="left",expand=False)
canvas.create_window((0,0),window=frame,anchor=NW)
vbar=tk.Scrollbar(root)

canvas.create_rectangle(0,0,1500,2500,fill='lightcoral')
#putting image
photo1=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\monument.png")
photo1=photo1.subsample(3,3)
canvas.create_image(300,110,image=photo1)
#putting image
photo2=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\AB1.png")
photo2=photo2.subsample(4,4)
canvas.create_image(980,110,image=photo2)

info="""BUILDINGS"""
canvas.create_text(540,160,fill="navajowhite",font="Times 20 italic bold",text=info)
#info
info="""Velore Institute of Technology,Chennai  was established in the year 2010. A striking feature of VIT is the well-planned and comprehensive\n infrastructure provided for both students and faculty. There are two academic blocks in VIT which are extremely specialised in their own particular field,\n namely- AB1 and AB2. The layout\has been excellently planned to make the maximum utilisation of the campus. The idea behind these separate blocks is to make every block equipped with the \nnecessary amenities whilst providing the perfect atmosphere for both studies and research.
  """
#display text
canvas.create_text(800,320,fill="purple",font="Times 15 italic",text=info)
i=0

def video():
   os.system(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\cam.mp4")
var = IntVar()
rb1 = Button(root, text= "Play Video",bg='violet', command=video).place(x=540,y=180)


#gallery

conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
with conn:
   cur=conn.cursor()




def extract_picture(cursor, picture_id,y):
    sql = "SELECT pic, name,info FROM buildings WHERE pic_id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, afile,desc = cursor.fetchone()
    ext='.png'
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    canvas.create_text(600,y,fill="gold",font="Times 19 italic bold",text=afile)
    y=y+50
    canvas.create_text(600,y,fill="lightblue",font="Times 19 italic bold",text=desc,anchor=NW)
    y=y+100
   
    
    return ablob

conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
cur = conn.cursor()
y=300
#filename = extract_picture(cur,2001,y)

#photo2=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\diseno.jpg")
#photo2=photo2.subsample(2,2)
#canvas.create_image(980,500,image=photo2)
#y=y+200
#filename = extract_picture(cur,2002,y)
#photo2=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\foosball.png")
#photo2=photo2.subsample(2,2)
#canvas.create_image(980,500,image=photo2)

y=y+200
filename = extract_picture(cur,1007,y)
photo3=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\A_block.png")
photo3=photo3.subsample(2,2)
canvas.create_image(260,550,image=photo3)

y=y+300
filename = extract_picture(cur,1001,y)
photo4=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\AB1.png")
photo4=photo4.subsample(3,3)
canvas.create_image(260,850,image=photo4)

y=y+300
filename = extract_picture(cur,1002,y)
photo5=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\ADMIN_BLOCK.png")
photo5=photo5.subsample(3,3)
canvas.create_image(260,1150,image=photo5)

y=y+300
filename = extract_picture(cur,1012,y)
photo6=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\monument.png")
photo6=photo6.subsample(2,6)
canvas.create_image(260,1450,image=photo6)

y=y+250
filename = extract_picture(cur,1003,y)
photo7=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\auditorium.png")
canvas.create_image(260,1700,image=photo7)

y=y+300
filename = extract_picture(cur,1013,y)
photo8=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\Basket.png")
photo8=photo8.subsample(4,4)
canvas.create_image(260,2000,image=photo8)





cur.close()
conn.close() 








root.mainloop()
