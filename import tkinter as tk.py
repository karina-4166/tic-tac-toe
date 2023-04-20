from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("Welcome")

def tic_tac_toe():
    def createboard(x,z):
        zero = 'X' if x[0] else ('0' if z[0] else 0 )
        one = 'X' if x[1] else ('0' if z[1] else 1 )
        two = 'X' if x[2] else ('0' if z[2] else 2 )
        three = 'X' if x[3] else ('0' if z[3] else 3 )
        four = 'X' if x[4] else ('0' if z[4] else 4 )
        five = 'X' if x[5] else ('0' if z[5] else 5 )
        six = 'X' if x[6] else ('0' if z[6] else 6 )
        seven = 'X' if x[7] else ('0' if z[7] else 7 )
        eight = 'X' if x[8] else ('0' if z[8] else 8 )

        print(f" {zero} | {one} | {two} ")
        print(f"---|---|---")
        print(f" {three} | {four} | {five} ")
        print(f"---|---|---")
        print(f" {six} | {seven} | {eight} ")

    print("WELCOME TO TIC TAC TOE")

    x = [0,0,0,0,0,0,0,0,0]
    z = [0,0,0,0,0,0,0,0,0]
    turn = 1 #1 for x and 0 for O
    while(True):
        createboard(x,z)
        if turn == 1:
            print("X's Chance = ")
            value = int(input("Please enter a value = "))
            x[value] = 1
        else:
            print("0's Chance = ")
            value = int(input("Please enter a value = "))
            z[value] = 1
        turn = 1 - turn

label1=Label(window,text="welcome to Tic Tac Toe.", fg='yellow', bg='red', relief='solid', font=("arial",20,"bold"))
label1.pack(pady=0.5,padx=0.5)
button1=Button(window,text="Press to start", fg='yellow',bg='Blue',command=tic_tac_toe)
button1.place(x=200,y=150)
window.mainloop()