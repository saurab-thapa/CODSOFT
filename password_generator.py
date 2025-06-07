import random
import string
import time

#PASSWORD GENERATOR PROGRAM

print("___WELCOME TO PASSWORD GENERATOR___")

def pass_gen(pass_len):
    password=''
    characters=string.ascii_letters+string.digits+string.punctuation
    for len in range(pass_len):
        password+=(random.choice(characters))
    print("Your password is being is processed...")
    time.sleep(2)
    print(f"Your password is   :   {password}")

def main():
    while True:
        try:
            length=int(input("Enter length for your password : "))
            if length<5:
                print("The length cannot be less than 5")
            else:
                break
        except ValueError:
            print("Please enter a numeric value")
    ans='y'
    while ans!='n':
        pass_gen(length)
        ans=input("Suggest another password (Y/N) : ").lower()

main()







#PASSWORD GENERATOR GUI

"""
import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Password Generator")
window.geometry('200x200')


password=tk.StringVar()

def gen_pass():
    pw=""
    try:
        length=int(len_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter a valid integer")
        return
        
    if length<5:
            messagebox.showerror("Invalid Input","Length cannot be less than 5 characters")
            return
    characters=string.ascii_letters+string.digits+string.punctuation
    for i in range(int(length)):
        pw+=random.choice(characters)
    password.set(pw)
           
    

lab1=tk.Label(window,text="Enter the length of your password")
lab1.grid(row=0,column=0,padx=10,pady=5)

len_entry=tk.Entry(window,width=20)
len_entry.grid(row=1,column=0,padx=10,pady=5)

gen_btn=tk.Button(window,text="Generate Password",command=gen_pass)
gen_btn.grid(row=2,column=0,padx=10,pady=15)

lab2=tk.Label(window,text="Your password is ")
lab2.grid(row=3,column=0,padx=10,pady=5)

pass_entry=tk.Entry(window,textvariable=password,width=20)
pass_entry.grid(row=4,column=0,padx=10,pady=5)

window.mainloop()

"""