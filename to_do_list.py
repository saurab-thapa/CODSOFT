import tkinter as tk
import mysql.connector
from tkinter import messagebox

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="to_do_rec"
)

mycur=conn.cursor()

window=tk.Tk()
window.title("To-Do List")

def add_task():
    task=task_entry.get()
    if task=="":
        messagebox.showerror("Input Error","No task entered")
        return
    mycur.execute("INSERT INTO tasks (task) values (%s)",(task,))
    conn.commit()
    task_entry.delete(0,tk.END)
    display_task()
    
def display_task():
    task_list.delete(0,tk.END)
    mycur.execute("SELECT * FROM tasks")
    for task in mycur.fetchall():
        display=f"{task[0]}. {task[1]} [{task[2]}]"
        task_list.insert(tk.END,display)

def mark_comp():
    selected=task_list.curselection()
    if not selected:
        messagebox.showerror("Selection Error","No item selected")
    else:
        text=task_list.get(selected[0])
        id=text.split(".")[0]
        mycur.execute("UPDATE tasks SET status='Completed' WHERE id=%s",(id,))
        conn.commit()
        display_task()
        
def del_task():
    selected=task_list.curselection()
    if not selected:
        messagebox.showerror("Selection Error","No item selected")
    else:
        text=task_list.get(selected[0])
        id=text.split(".")[0]
        mycur.execute("DELETE FROM tasks WHERE id=%s",(id,))
        conn.commit()
        display_task()
        
    

task_entry=tk.Entry(window,width=50)
task_entry.grid(row=0,column=0,padx=10,pady=10)

add_btn=tk.Button(window,text="Add Task",command=add_task)
add_btn.grid(row=0,column=1,padx=10,pady=10)

task_list=tk.Listbox(window,width=70)
task_list.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

comp_btn=tk.Button(window,text="Mark as Done",command=mark_comp)
comp_btn.grid(row=2,column=0,sticky='w',padx=10,pady=10)

del_btn=tk.Button(window,text="Delete task",command=del_task)
del_btn.grid(row=2,column=1,sticky='e',padx=10,pady=10)

display_task()
window.mainloop()
