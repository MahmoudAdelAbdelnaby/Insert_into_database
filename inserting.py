# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:30:38 2022

@author: Abdelnaby
"""

import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
from PIL import ImageTk,Image
import urllib   
from sqlalchemy import create_engine
import pyodbc 
import datetime
from datetime import datetime

server = 'localhost\sqlexpress' 
database = 'master' 
username = 'mahmoud' 
password = '1234' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

connection_string = "DRIVER={SQL Server};Database=master;SERVER=localhost\sqlexpress;UID=mahmoud;PWD=1234"
connection_string = urllib.parse.quote_plus(connection_string) 
connection_string = "mssql+pyodbc:///?odbc_connect=%s" % connection_string
engine = create_engine(connection_string)

df = pd.read_sql_query('''SELECT TOP (1000) [Name]
      ,[NT]
      ,[position]
      ,[skill]
      ,[approved]
      ,[Date]
  FROM [master].[dbo].[Python_Test]''',con = engine)
   
def Validate(string,whitelist = ("%Y/%m/%d","%Y-%m-%d","%Y%m%d")):
    for fmt in whitelist:
        try:
            dt = datetime.strptime(string, fmt)
        except ValueError:
            pass
        else : 
            return True
    else:
        return False

    
    
def Inserting1():
    try :
        Name_input = e1.get()
        NT_input = e2.get()
        position_input = e3.get()
        skill_input = e4.get()
        approved_input = e5.get()
        date_input = e6.get()
        if Name_input == '':
            tk.messagebox.showerror("Warning", "Name Box Cant be blank")
        elif NT_input == '':
            tk.messagebox.showerror("Warning", "NT Box Cant be blank")
        elif position_input == '':
            tk.messagebox.showerror("Warning", "Position Box Cant be blank")
        elif skill_input == '':
            tk.messagebox.showerror("Warning", "Skill Box Cant be blank")
        elif approved_input == '':
            tk.messagebox.showerror("Warning", "Approved Box Cant be blank")
        elif date_input == '':
            tk.messagebox.showerror("Warning", "Date Box Cant be blank")
        elif not bool(Validate(date_input)):
            tk.messagebox.showerror("Warning", "Date can only be YYYY-MM-DD or YYYY/MM/DD or YYYYMMDD")
        else:
            global Data_base 
            global myLabel
            Data_base = query_text.get()
            myLabel.destroy()
            e1.delete(0,'end')
            e2.delete(0,'end')
            e3.delete(0,'end')
            e4.delete(0,'end')
            e5.delete(0,'end')
            e6.delete(0,'end')
            cursor = cnxn.cursor()
            cursor.execute(f'''
      insert into [dbo].[{Data_base}]([Name]
      ,[NT]
      ,[position]
      ,[skill]
      ,[approved]
      ,[Date])
 	  values(?,?,?,?,?,?)''',Name_input,NT_input,position_input,skill_input,approved_input,date_input)
            cnxn.commit()
            myLabel = Label(root,text = 'Row Added',fg ='green')
            myLabel.grid(row =14,column = 1)
            
    except :
        raise
        # myLabel2 = Label(root,text = 'Something went wrong',fg ='Red')
        # myLabel2.grid(row =14,column = 2)
        # e1.delete(0,'end')
        # e2.delete(0,'end')
        # e3.delete(0,'end')
        # e4.delete(0,'end')
        # e5.delete(0,'end')
        # e6.delete(0,'end')
        
        
def Inserting2():
    try :
        Name_input = e7.get()
        NT_input = e8.get()
        position_input = e9.get()
        skill_input = e10.get()
        approved_input = e11.get()
        date_input = e12.get()
        if Name_input == '':
            tk.messagebox.showerror("Warning", "Name Box Cant be blank")
        elif NT_input == '':
            tk.messagebox.showerror("Warning", "NT Box Cant be blank")
        elif position_input == '':
            tk.messagebox.showerror("Warning", "Position Box Cant be blank")
        elif skill_input == '':
            tk.messagebox.showerror("Warning", "Skill Box Cant be blank")
        elif approved_input == '':
            tk.messagebox.showerror("Warning", "Approved Box Cant be blank")
        elif date_input == '':
            tk.messagebox.showerror("Warning", "Date Box Cant be blank")
        elif not bool(Validate(date_input)):
            tk.messagebox.showerror("Warning", "Date can only be YYYY-MM-DD or YYYY/MM/DD or YYYYMMDD")
        else:
            global Data_base 
            global myLabel
            Data_base = query_text.get()
            myLabel.destroy()
            e7.delete(0,'end')
            e8.delete(0,'end')
            e9.delete(0,'end')
            e10.delete(0,'end')
            e11.delete(0,'end')
            e12.delete(0,'end')
            cursor = cnxn.cursor()
            cursor.execute(f'''
      insert into [dbo].[{Data_base}]([Name]
      ,[NT]
      ,[position]
      ,[skill]
      ,[approved]
      ,[Date])
 	  values(?,?,?,?,?,?)''',Name_input,NT_input,position_input,skill_input,approved_input,date_input)
            cnxn.commit()
            myLabel = Label(root,text = 'Row Added',fg ='green')
            myLabel.grid(row =14,column = 1)
            
    except :
        raise
        # myLabel2 = Label(root,text = 'Something went wrong',fg ='Red')
        # myLabel2.grid(row =14,column = 2)
        # e1.delete(0,'end')
        # e2.delete(0,'end')
        # e3.delete(0,'end')
        # e4.delete(0,'end')
        # e5.delete(0,'end')
        # e6.delete(0,'end')        
root = Tk()

myLabel = Label(root)
myLabel2 = Label(root)
myLabel3 = Label(root)


root.title('inserting into database')
root.geometry("410x550")

### uncomment and add your img if you need to add an img was resized to fit the geometry of the canvas ###
# my_img = Image.open("insert your img path here")
# resized_image= my_img.resize((400,205), Image.ANTIALIAS)
# New_img = ImageTk.PhotoImage(resized_image)
# my_label = Label(image = New_img)
# my_label.pack()


def hide(choice): 
    if choice == 'Select From list':
        global Box1
        global e1
        global Box2
        global e2
        global Box3
        global e3
        global Box4
        global e4
        global Box5
        global e5
        global Box6
        global e6
        global Box7
        global e7
        global Box8
        global e8
        global Box9
        global e9
        global Box10
        global e10
        global Box11
        global e11
        global Box12
        global e12
        global myButton2
        global myButton3
        Box1.grid_remove()
        e1.grid_remove()
        Box2.grid_remove()
        e2.grid_remove()
        Box3.grid_remove()
        e3.grid_remove()
        Box4.grid_remove()
        e4.grid_remove()
        Box5.grid_remove()
        e5.grid_remove()
        Box6.grid_remove()
        e6.grid_remove()
        myButton2.grid_remove()
        Box7.grid_remove()
        e7.grid_remove()
        Box8.grid_remove()
        e8.grid_remove()
        Box9.grid_remove()
        e9.grid_remove()
        Box10.grid_remove()
        e10.grid_remove()
        Box11.grid_remove()
        e11.grid_remove()
        Box12.grid_remove()
        e12.grid_remove()
        myButton2.grid_remove()
        myButton3.grid_remove()
        myLabel.destroy()
    elif choice == "Python_Test":
        Box1 = tk.Label(root,text = "Enter your name:")
        Box1.grid(row =1, column = 1)

        e1 = tk.Entry(root)
        e1.grid(row =2,column = 1)

        Box2 = tk.Label(root,text = "Enter your NT")
        Box2.grid(row =3,column = 1)

        e2 = tk.Entry(root)
        e2.grid(row =4,column = 1)

        Box3 = tk.Label(root,text = "Enter your position :")
        Box3.grid(row =5,column = 1)

        e3 = tk.Entry(root)
        e3.grid(row =6,column = 1)

        Box4 = tk.Label(root,text = "Enter your skills :")
        Box4.grid(row =7,column = 1)

        e4 = tk.Entry(root)
        e4.grid(row =8,column = 1)

        Box5 = tk.Label(root,text = "Approved (Yes/No):")
        Box5.grid(row =9,column = 1)

        e5 = tk.Entry(root)
        e5.grid(row =10,column = 1)

        Box6 = tk.Label(root,text = "Enter Date (YYYY/MM/DD):")
        Box6.grid(row =11,column = 1)

        e6 = tk.Entry(root)
        e6.grid(row =12,column = 1)
        myButton2 = Button(root,command = Inserting1,text = "insert into Database")
        myButton2.grid(row =13,column = 1) 
        myLabel.destroy()
    elif choice == "Python_Test2":
        Box7 = tk.Label(root,text = "Enter your name:")
        Box7.grid(row =1, column = 1)

        e7 = tk.Entry(root)
        e7.grid(row =2,column = 1)

        Box8 = tk.Label(root,text = "Enter your NT")
        Box8.grid(row =3,column = 1)

        e8 = tk.Entry(root)
        e8.grid(row =4,column = 1)

        Box9 = tk.Label(root,text = "Enter your position :")
        Box9.grid(row =5,column = 1)

        e9 = tk.Entry(root)
        e9.grid(row =6,column = 1)

        Box10 = tk.Label(root,text = "Enter your skills :")
        Box10.grid(row =7,column = 1)

        e10 = tk.Entry(root)
        e10.grid(row =8,column = 1)

        Box11 = tk.Label(root,text = "Approved (Yes/No):")
        Box11.grid(row =9,column = 1)

        e11 = tk.Entry(root)
        e11.grid(row =10,column = 1)

        Box12 = tk.Label(root,text = "Enter Date (YYYY/MM/DD):")
        Box12.grid(row =11,column = 1)

        e12 = tk.Entry(root)
        e12.grid(row =12,column = 1)
        myButton3 = Button(root,command = Inserting2,text = "insert into Database")
        myButton3.grid(row =13,column = 1)
        myLabel.destroy()

    
options = ["Select From list",'Python_Test','Python_Test2']

query_text = StringVar()
query_text.set(options[0])
lblname = Label(root, font=("arial", 10, "bold"), text="Query/Reply", bd=8, anchor="w")
lblname.grid(row=0, column=0)
txtname28 = OptionMenu(root, query_text, *options, command=hide)
txtname28.grid(row=0, column=1)



## button that will fire the predicting function ##

    

root.mainloop()
