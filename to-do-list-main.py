"""Lets work on creating a canvas on left with the check-buttons as we cant add them in the table"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysqlpasskey import passkey

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= passkey ,
    database= "todoapp"
)
cursor=mydb.cursor()
class Task:
    def __init__(self,id,name,discription='NULL', date='NULL'):
        self.id=id
        self.name=name
        self.discription=discription
        self.date=date
    def add_task (self):
        try :
            
            query = "INSERT INTO todolist (id,name,discription,duedate) values(%s,%s,%s,%s)"
            values = (self.id,self.name,self.discription,self.date)
            cursor.execute(query, values)
            # mydb.commit()
        except:
            return "Sorry record could not be added, please check format!"
        else:
            return "Sorry please check input"
    def show_task (self):
        try:
            show_query="select * from todolist where name=%s;"
            task_name=(self.name,)
            cursor.execute(show_query,task_name)
            result=cursor.fetchall()
            return result
        except:
             return "Sorry"
        
        
             
# new_task=Task(11,"11","11","2023-08-28")
# new_task.add_task()
# print(new_task.show_task())
def show_all_tasks ():
        try:   
            show_query="select * from todolist order by duedate;"
            cursor.execute(show_query)
            result=cursor.fetchall()
            for row in tree.get_children():
                tree.delete(row)
            for record in result:
                tree.insert('','end',values=(record))
            # i=1
            # for record in result:
                
            #     tk.Checkbutton(mainWindow, text='', variable=id).grid(row=i, column=0)
            #     tree.insert('', 'end', values=(False, *record))
            #     i+=1

        except:
             return "Sorry"
        
def del_task(name_of_task):
    try:
        del_query="delete from todolist where name=%s ;"
        name_tuple=(name_of_task,)
        cursor.execute(del_query,name_tuple)
        show_all_tasks()
        mydb.commit()
    except:
        return "Sorry"
#del_task('eat')

def complete_task(name):
    try:    
        name_tuple=(name,)
        complete_query_1="insert into completed_tasks select * from todolist where name=%s;"
        cursor.execute(complete_query_1,name_tuple)
        complete_query_2="delete from todolist where name=%s;"
        cursor.execute(complete_query_2,name_tuple)
        mydb.commit()
    except:
        return "Sorry"

def on_select():
    print("hello")
    pass
#complete_task("move-in2") #move-in2 has already been completed, use another name while trying it

#main window
mainWindow=tk.Tk()
#mainWindow.title="To-Do List!"

#all the code for the tkinter module goes here

mainWindow.title("To-Do Application!")
mainWindow.geometry("600x500")
close_button=tk.Button(mainWindow,text="close window!",command=mainWindow.destroy, activebackground='Red', bg='Blue')
close_button.grid(row=0,column=1)
# newbutton=tk.Button(mainWindow,text="Print",command=lambda: print("See this worked!"))
# newbutton.grid(row=2,column=0)
# name_lable=Label(text="Name")
# name_lable.grid(row=3,column=1,columnspan=2)
# description_lable=Label(text="Discription")
# description_lable.grid(row=3,column=3,columnspan=2)
# due_date_lable=Label(text="Due-Date")
# due_date_lable.grid(row=3,column=12,columnspan=2)
# show_button=Button(text="Show tasks",command=show_all_tasks)

# Create a Treeview widget
tree = ttk.Treeview(mainWindow, columns=('ID', 'Name', 'Description','due_date'), show='headings')

# Set column headings

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Description', text='Description')
tree.heading('due_date',text='due_date')

# Set column widths

tree.column('ID', width=50)
tree.column('Name', width=150)
tree.column('Description',width=200)
tree.column('due_date',width=150)

# Add a button to retrieve data and display it in the table
fetch_button = tk.Button(mainWindow, text='Fetch Data', command=show_all_tasks())
#fetch_button.pack(pady=10)
fetch_button.grid(row=0,column=3,pady=10)
# Pack the Treeview widget
#tree.pack(fill='both', expand=True)
tree.grid(row=1,column=1,columnspan=50)




mainWindow.mainloop()

     
cursor.close()
mydb.close()       

