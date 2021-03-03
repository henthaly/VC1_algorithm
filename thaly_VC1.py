import tkinter as tk
import random
from tkinter import *
# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("650x700")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Tkinter Draw")
canvas = tk.Canvas(frame)

# Create image
my_wall=tk.PhotoImage(file="wall.png")
bg=tk.PhotoImage(file="koya.png")
animie1=tk.PhotoImage(file="animie1.png")
part1=canvas.create_image(60,180,image=animie1)
diamond=tk.PhotoImage(file="diamond.jpg")
killer=tk.PhotoImage(file="animie1.png")
background=tk.PhotoImage(file="diamond1.jpg")
My_back=canvas.create_image(200,350,image=background)
#create the  wall
X=20
Y=50
Cell_wall=1
Cell_nothing=0
Cell_killer=8
Cell_diamond=4
player_score=0
my_array=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,"k",0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,8,1,4,0,0,0,1,8,1,0,0,1],
          [1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1],
          [1,0,1,0,0,0,0,0,0,1,8,0,1,0,0,1],
          [1,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1],
          [1,0,0,0,8,0,0,8,0,0,0,0,0,0,0,1],
          [1,0,0,4,0,0,1,4,0,1,0,0,0,0,0,1],
          [1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1],
          [1,0,8,1,0,1,0,0,1,8,0,0,0,0,0,1],
          [1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
          [1,0,1,8,0,1,0,1,0,1,0,0,0,1,0,1],
          [1,0,1,1,1,1,0,1,0,0,8,1,0,0,0,1],
          [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
          
def create_wall():
    global X,Y
    for n in range(len(my_array)):
        for i in range(len(my_array[n])):
            if my_array[n][i]==1:
                canvas.create_image(X,Y,image=my_wall)
            if my_array[n][i]==8:
                canvas.create_image(X,Y,image=diamond)
            if my_array[n][i]==4:
                canvas.create_image(X,Y,image=killer)
            X+=40
        Y+=40
        X=20
create_wall()

#Create player
Player=canvas.create_image(60,90,image=bg)


# Player can move left,right,up,dow

def right():
    global my_array
    player= position()
    Row=player[0]
    Col=player[1]
    right=my_array[Row][Col+1]
    result=canMove(right)
    return result
player_X=0
player_Y=0
def move_player():
    global player_X,player_Y,Player
    canvas.move(Player,player_X,player_Y)
    
def board_left(event):
    global player_X,player_Y
    player_X=-20
    move_player()
    player_X=0
def board_right(event):
    global player_X,player_Y
    player_X=+20
    move_player()
    right()
    player_X=0
def board_up(event):
    global player_X,player_Y
    player_Y=-20
    move_player()
    player_Y=0
def board_down(event):
    global player_X,player_Y
    player_Y=+20
    move_player()
    player_Y=0


# Manage animies
condition=True
Y=0
# Animie area which animie can move
def animie1_move():
    global Y,condition
    if Y<=380 and condition==True:
        Y+=20
        canvas.after(100,lambda:animie1_move())
        canvas.move(part1,0,10)
    else:
        condition=False
        Y-=20
        canvas.after(100,lambda:animie1_move())
        canvas.move(part1,-0,-10)
        if Y==0:
           condition=True



animie2=tk.PhotoImage(file="animie1.png")
part2=canvas.create_image(300,250,image=animie2)
X1=0
condition1=True
def animie2_move():
    global X1,condition1
    if X1<=300 and condition1==True:
        X1+=20
        canvas.after(100,lambda:animie2_move())
        canvas.move(part2,10,0)
    else:
        condition1=False
        X1-=20
        canvas.after(100,lambda:animie2_move())
        canvas.move(part2,-10,0)
        if X1==0:
           condition1=True

animie3=tk.PhotoImage(file="animie1.png")
part3=canvas.create_image(550,300,image=animie3)
Y=0
condition=True
def animie3_move():
    global Y,condition
    if Y<=500 and condition==True:
        Y+=20
        canvas.after(100,lambda:animie3_move())
        canvas.move(part3,0,10)
    else:
        condition=False
        Y-=20
        canvas.after(100,lambda:animie3_move())
        canvas.move(part3,-0,-10)
        if Y==0:
            condition=True
animie4=tk.PhotoImage(file="animie1.png")
part4=canvas.create_image(60,570,image=animie4)
X=0
condition1=True
def animie4_move():
    global X,condition1
    if X<=400 and condition1==True:
        X+=20
        canvas.after(100,lambda:animie4_move())
        canvas.move(part4,10,0)
    else:
        condition1=False
        X-=20
        canvas.after(100,lambda:animie4_move())
        canvas.move(part4,-10,0)
        if X==0:
           condition1=True


canvas.after(500,lambda:animie1_move())
canvas.after(500,lambda:animie2_move())
canvas.after(500,lambda:animie3_move())
canvas.after(500,lambda:animie4_move())
root.bind("<Right>", board_right)
root.bind("<Left>", board_left)
root.bind("<Up>", board_up)
root.bind("<Down>", board_down)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()