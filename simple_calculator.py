#SIMPLE CALCULATOR PROGRAM

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
        
    
def calculator():
    print("\n------CALCULATOR------\n")
    while True:
        try:
            num1=float(input("Enter first number : "))
            num2=float(input("Enter second number : "))
            print()
            while True:
                choice=input("Choose an operation [ +  -  *  / ] : ").strip()
                if choice=="+":
                    result=add(num1,num2)
                    print(f"\nResult = {result}")
                    break
                elif choice=="-":
                    result=sub(num1,num2)
                    print(f"\nResult = {result}")
                    break
                elif choice=="*":
                    result=mul(num1,num2)
                    print(f"\nResult = {result}")
                    break
                elif choice=="/":
                    result=div(num1,num2)
                    print(f"\nResult = {result}")
                    break
                else:
                    print("Invalid operation")
            print()
            ans=input("Continue (Y/N) : ").strip()
            print()
            if ans.lower()!='y':
                break    
        except ValueError:
            print("Please enter numeric value\n")
             

calculator()













#SIMPLE CALCULATOT GUI 

'''
import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Calculator")

result=tk.StringVar()

label1=tk.Label(window,text="Enter number")
label1.grid(row=0,column=0,columnspan=1,padx=5,pady=10)

user_input_1=tk.Entry(window,width=30)
user_input_1.grid(row=0,column=1,columnspan=4,padx=5,pady=10)

label2=tk.Label(window,text="Enter number")
label2.grid(row=1,column=0,columnspan=1,padx=5,pady=10)

user_input_2=tk.Entry(window,width=30)
user_input_2.grid(row=1,column=1,columnspan=4,padx=5,pady=10)


def add():
    num1=user_input_1.get()
    num2=user_input_2.get()
    if num1=="" or num2=="":
        messagebox.showerror("Input Error","Input not Found")
    sum=float(num1)+float(num2)
    result.set(sum)
    
    
def sub():
    num1=user_input_1.get()
    num2=user_input_2.get()
    if num1=="" or num2=="":
        messagebox.showerror("Input Error","Input not Found")
    diff=float(num1)-float(num2)
    result.set(diff)
    
def mul():
    num1=user_input_1.get()
    num2=user_input_2.get()
    if num1=="" or num2=="":
        messagebox.showerror("Input Error","Input not Found")
    prod=float(num1)*float(num2)
    result.set(prod)
    
def div():
    num1=user_input_1.get()
    num2=user_input_2.get()
    if num1=="" or num2=="":
        messagebox.showerror("Input Error","Input not Found")
    if float(num2)==0:
        messagebox.showerror("Zero Division Error","Division by zero is not allowed")
        user_input_2.delete(0,tk.END)
        return
    else:
        quot=float(num1)/float(num2)
        result.set(f"{quot:.5f}")
    
add_btn=tk.Button(window,text="+",width=3,command=add,fg='white',bg='green')
add_btn.grid(row=2,column=0,padx=3,pady=10)

sub_btn=tk.Button(window,text="-",width=3,command=sub,fg='white',bg='green')
sub_btn.grid(row=2,column=1,padx=25,pady=10)

mul_btn=tk.Button(window,text="*",width=3,command=mul,fg='white',bg='green')
mul_btn.grid(row=2,column=2,padx=25,pady=10)

div_btn=tk.Button(window,text="/",width=3,command=div,fg='white',bg='green')
div_btn.grid(row=2,column=3,padx=25,pady=10)

res_label=tk.Label(window,text="Result")
res_label.grid(row=3,column=0,padx=10,pady=10)

res_output=tk.Entry(window,textvariable=result,width=30)
res_output.grid(row=3,column=1,columnspan=4,padx=10,pady=10)

window.mainloop()
'''

