import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image
from io import BytesIO
import base64
import numpy as np
import sys
import mainpage_2 
import buildings
import events
import os
#sys.setdefaultencoding("ISO-8859-1")

#C:\Users\PANKAJ\AppData\Local\Programs\Python\Python37-32\Scripts

x=710
y=500
root = tk.Tk()
root.geometry('1000x600')
root.title("Commitees")

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
   canvas=Canvas(width=1500,height=6500)
   canvas.config(scrollregion=canvas.bbox("all"))
   vscrollbar.config(command=canvas.yview)
   vscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
   frame=tk.Frame(canvas)
   canvas.pack(side="left",expand=False)
   canvas.create_window((0,0),window=frame,anchor=NW)
   vbar=tk.Scrollbar(root)
   
   canvas.create_rectangle(0,0,1500,3500,fill='olivedrab1')
   #putting image_
   photo1=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Connectivity.png")
   photo1=photo1.subsample(3,3)  
   canvas.create_image(300,110,image=photo1)
   #putting image
   photo2=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Qubit.png")
   photo2=photo2.subsample(2,2)
   canvas.create_image(980,110,image=photo2)

   info="""COMMITEES"""
   canvas.create_text(620,160,fill="black",font="Times 16 italic bold",text=info)
   #info
   info="""Velore Institute of Technology, Chennai is home to many gifted students with the potential to achieve a great many things.\n The various commitees in VIT are always on the lookout for fresh talent and are bent\n on utilising it reach great heights.The various commitees such as music, zuura, Shaurya etc handle \n  affairs such ranging from music to racing etc, """
   #display text
   canvas.create_text(650,320,fill="purple",font="Times 16 italic",text=info)
   i=0
   #gallery

   conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
   with conn:
      cur=conn.cursor()




def extract_picture(cursor, picture_id,y):
    sql = "SELECT pic, name,s_head,f_head,descrition FROM commitees WHERE pic_id = :id"
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
    canvas.create_text(580,y,fill="black",font="Times 19 italic bold",text=desc,anchor=NW)

   
    
    return ablob

conn = sqlite3.connect(r"C:\\sqlite\db\pythonsqlite.db")
cur = conn.cursor()
y=250
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
filename = extract_picture(cur,3001,y)
photo3=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Connectivity.png")
photo3=photo3.subsample(3,3)
canvas.create_image(260,550,image=photo3)

y=y+300
filename = extract_picture(cur,3002,y)
photo4=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Diseno.png")
photo4=photo4.subsample(3,3)
canvas.create_image(260,850,image=photo4)

y=y+300
filename = extract_picture(cur,3004,y)
photo5=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Qubit.png")
photo5=photo5.subsample(3,3)
canvas.create_image(260,1150,image=photo5)

y=y+300
filename = extract_picture(cur,3005,y)
photo6=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Zuura.png")
photo6=photo6.subsample(2,3)
canvas.create_image(260,1450,image=photo6)

y=y+250
filename = extract_picture(cur,3006,y)
photo7=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Enactus.png")
photo7=photo7.subsample(3,3)
canvas.create_image(260,1700,image=photo7)

y=y+300
filename = extract_picture(cur,3007,y)
photo8=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Music.png")
photo8=photo8.subsample(3,3)
canvas.create_image(260,2000,image=photo8)

y=y+300
filename = extract_picture(cur,3008,y)
photo9=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\SAE.png")
photo9=photo9.subsample(3,3)
canvas.create_image(260,2280,image=photo9)

y=y+300
filename = extract_picture(cur,3003,y)
photo10=PhotoImage(file=r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Shaurya.png")
photo10=photo10.subsample(3,3)
canvas.create_image(260,2570,image=photo8)


cur.close()
conn.close() 








root.mainloop()
