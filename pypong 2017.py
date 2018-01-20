from Tkinter import *
from random import randint

root=Tk()
root.title("pypong")

paper = Canvas(root,width=300,height=300,background="white")

paddle=paper.create_rectangle(10,130,20,170,fill="red")
paddle2=paper.create_rectangle(280,130,290,170,fill="blue")

def moveup (event):
        paper.move(paddle,0,-10)

def moveup2 (event):
       paper.move(paddle2,0,-10)

def movedown (event):
       paper.move(paddle,0,10)

def movedown2 (event):
       paper.move(paddle2,0,10)

root.bind("w",moveup)
root.bind("s",movedown)
root.bind("<Up>",moveup2)
root.bind("<Down>",movedown2)

ball=paper.create_oval(5,5,15,15,fill="yellow")

#def move_ball (event=None):
       #paper.move(ball,10,10)
   #    paper.after(100,move_ball)


c_height,c_width=295,295
ballx,bally=0, 0
balldx,balldy=5, 5
rndx=randint(0,5)
rndy=randint(0,5)


def move_ball():
                  global ballx,bally
                  global balldx,balldy

                  if ballx<10:
                     balldx=(balldx+rndx)
                     
                  if ballx>c_width:
                     balldx=-(balldx+rndx)

                  if bally<10:
                     balldy=(balldy+rndy)

                  if bally>c_height:
                     balldy=-(balldy+rndy)

                  ballx+=balldx
                  bally+=balldy
                  paper.move(ball,balldx,balldy)
                  paper.after(100,move_ball)




move_ball()

paper.pack()
root.mainloop()
