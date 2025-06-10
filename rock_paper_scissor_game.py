import random
import time

print("Welcome to Rock-Paper-Scissor Game\n")

def computer_choice():
    return random.choice(['rock','paper','scissor'])
    
def user_choice():
    choice=input("Enter your choice (rock, paper, scissor)  :  ").lower().strip()
    while choice not in ['rock','paper','scissor']:
        print("Invalid Choice")
        choice=input("Enter your choice (rock, paper, scissor)  :  ").lower().strip()
    return choice

def game():
    while True:
        user_point=0
        computer_point=0
        rounds_played=0
        while rounds_played<3:
            user=user_choice()
            computer=computer_choice()
            print("Wait for computer's choice")
            time.sleep(2)
            print("Computer's choice  :  ",computer)
            if(user==computer):
                print("That is a tie!\n")
                continue
            elif(user=='paper' and computer=='rock') or (user=='scissor' and computer=='paper') or (user=='rock' and computer=='scissor'):
                print("Yay! You got the point\n")
                user_point+=1
            else:
                print("Oho! Computer gets the point\n")
                computer_point+=1
            rounds_played+=1
        print("_____Final Result_____")
        print("Your points  :  ",user_point)
        print("Computer's points  :  ",computer_point)
        if user_point>=2 or computer_point>=2:
            if user_point>computer_point:
                print("Hurrah! You won :) \n")
            else:
                print("Oh no! Computer won :( \n")
        ans=input("Play again (Y/N)  :  ").lower().strip()
        print()
        if ans=="n":
            break
        
game()


#ROCK_PAPER_SCISSOR_GAME_GUI

"""
import random
import tkinter as tk

window=tk.Tk()
window.title("Game")
window.config(bg="light blue")

user_choice=tk.StringVar()
comp_choice=tk.StringVar()
result=tk.StringVar()

def winner(user,computer):
    if (user=="rock" and computer=="scissor") or (user=="paper" and computer=="rock") or (user=="scissor" and computer=="paper"):
        result.set("Hurrah! You won :)")
    elif (user==computer):
        result.set("That is a tie")
    else:
        result.set("You lost :(")

def game(choice):
    user_choice.set(choice.capitalize())
    computer=random.choice(["rock","paper","scissor"])
    comp_choice.set(computer.capitalize())
    winner(choice,computer)
    
lab1=tk.Label(window,text="Rock-Paper-Scissor Game",bg="light blue")
lab1.grid(row=0,column=0,columnspan=3,pady=10)

rock_btn=tk.Button(window,text="Rock",width=15,command=lambda: game("rock"))
rock_btn.grid(row=1,column=0,padx=10,pady=10)

paper_btn=tk.Button(window,text="Paper",width=15,command=lambda: game("paper"))
paper_btn.grid(row=1,column=1,padx=10,pady=10)

scissor_btn=tk.Button(window,text="Scissor",width=15,command=lambda: game("scissor"))
scissor_btn.grid(row=1,column=2,padx=10,pady=10)

user_lab1=tk.Label(window,text="Your choice : ",bg="light blue")
user_lab1.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

user_lab2=tk.Label(window,textvariable=user_choice,bg="light blue")
user_lab2.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

comp_lab1=tk.Label(window,text="Computer's choice : ",bg="light blue")
comp_lab1.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

comp_lab2=tk.Label(window,textvariable=comp_choice,bg="light blue")
comp_lab2.grid(row=3,column=1,columnspan=2,padx=10,pady=10)

res_lab1=tk.Label(window,text="Result : ",bg="light blue")
res_lab1.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

res_lab2=tk.Label(window,textvariable=result,bg="light blue")
res_lab2.grid(row=4,column=1,columnspan=2,padx=10,pady=10)

window.mainloop()

"""