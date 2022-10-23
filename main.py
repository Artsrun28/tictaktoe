import random
import tkinter as tk
from time import sleep


win = tk.Tk()
win.title("TicTakToe")
win.geometry("947x950")
win.configure(background="red")
win.resizable(width=False, height=False)


def user_win():
    pass


def lost():
    pass


def draw():
    pass


blank_img = tk.PhotoImage(file='images/blank.png')

img_o = tk.PhotoImage(file='images/o.png')
img_oh = tk.PhotoImage(file='images/oh.png')
img_ov = tk.PhotoImage(file='images/ov.png')
img_olr = tk.PhotoImage(file='images/olr.png')
img_orl = tk.PhotoImage(file='images/orl.png')

img_x = tk.PhotoImage(file='images/x.png')
img_xh = tk.PhotoImage(file='images/xh.png')
img_xv = tk.PhotoImage(file='images/xv.png')
img_xlr = tk.PhotoImage(file='images/xlr.png')
img_xrl = tk.PhotoImage(file='images/xrl.png')


#whit this i'm going to make one of the players win, lost or draw
#Ex if r1c1 r1c2 r1c3 == False someone won, or r1c1 r2c2 r3c3 == False someone won. there is a 8 combinatino to win
r1c1 = True
r1c2 = True
r1c3 = True
r2c1 = True
r2c2 = True
r2c3 = True
r3c1 = True
r3c2 = True
r3c3 = True


#With this list i'm keeping the count which rows and cells are empty and which are full
blank_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def button1_command():
    button1.configure(image=img_x)                  #it changes the background image of the button
    player1remove = blank_list.remove(1)            #it delets the cell which is being pushed, in order not to let computer to press it again
    global r1c1
    r1c1 = False
    sleep(0.2)                                      #i just want to make game slower
    player2 = random.choice(blank_list)             #whit this line player2 (computer) makes it's game. It's not that smart it's just doing random move. If i had a time, i may make it smarter
    player2remove = blank_list.remove(player2)      #and removes the cell where he has played
    if player2 == 2:                                #and from here it changes the button image from blank white cell to O, and also changes the bool variable to False
        button2.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button2_command():
    button2.configure(image=img_x)
    player1remove = blank_list.remove(2)
    global r1c2
    r1c2 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button3_command():
    button3.configure(image=img_x)
    player1remove = blank_list.remove(3)
    global r1c3
    r1c3 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button4_command():
    button4.configure(image=img_x)
    player1remove = blank_list.remove(4)
    global r2c1
    r2c1 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button5_command():
    button5.configure(image=img_x)
    player1remove = blank_list.remove(5)
    global r2c2
    r2c2 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button6_command():
    button6.configure(image=img_x)
    player1remove = blank_list.remove(6)
    global r2c3
    r2c3 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button7_command():
    button7.configure(image=img_x)
    player1remove = blank_list.remove(7)
    global r3c1
    r3c1 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button8_command():
    button8.configure(image=img_x)
    player1remove = blank_list.remove(8)
    global r3c2
    r3c2 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 9:
        button9.configure(image=img_o)
        global r3c3
        r3c3 = False


def button9_command():
    button9.configure(image=img_x)
    player1remove = blank_list.remove(9)
    global r3c3
    r3c3 = False
    sleep(0.2)
    player2 = random.choice(blank_list)
    player2remove = blank_list.remove(player2)
    if player2 == 1:
        button1.configure(image=img_o)
        global r1c1
        r1c1 = False
    elif player2 == 2:
        button3.configure(image=img_o)
        global r1c2
        r1c2 = False
    elif player2 == 3:
        button3.configure(image=img_o)
        global r1c3
        r1c3 = False
    elif player2 == 4:
        button4.configure(image=img_o)
        global r2c1
        r2c1 = False
    elif player2 == 5:
        button5.configure(image=img_o)
        global r2c2
        r2c2 = False
    elif player2 == 6:
        button6.configure(image=img_o)
        global r2c3
        r2c3 = False
    elif player2 == 7:
        button7.configure(image=img_o)
        global r3c1
        r3c1 = False
    elif player2 == 8:
        button8.configure(image=img_o)
        global r3c2
        r3c2 = False



#buttons: which ara also game characters. You can differ them with the images X and O

button1 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button1_command(),
    borderwidth=7
)
button1.grid(row=1, column=1)


#I coudnt manage to make button 2 work, i'ts just hidden
button2 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button2_command(),
    borderwidth=7
)
button2.grid(row=1, column=2)

button3 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button3_command(),
    borderwidth=7
)
button2.grid(row=1, column=3)

button4 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button4_command(),
    borderwidth=7
)
button4.grid(row=2, column=1)

button5 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button5_command(),
    borderwidth=7
)
button5.grid(row=2, column=2)

button6 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button6_command(),
    borderwidth=7
)
button6.grid(row=2, column=3)

button7 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button7_command(),
    borderwidth=7
)
button7.grid(row=3, column=1)

button8 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button8_command(),
    borderwidth=7
)
button8.grid(row=3, column=2)

button9 = tk.Button(
    win,
    image=blank_img,
    command=lambda: button9_command(),
    borderwidth=7
)
button9.grid(row=3, column=3)


win.mainloop()
