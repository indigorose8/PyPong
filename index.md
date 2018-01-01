# Python Pong worksheet

## Task 1 - The minimal tk canvas

The Pizza worksheet shows you how to make simple shapes, such as circles and rectangles, and shows you how to write functions that take parameters.

Remember the steps in making a minimal  tk canvas:
             
```python
        #import the libraries
        #create a top level object
        #attach a canvas
        #draw something
        #run the mainloop
```

See if you can write your own; if you get really stuck, use the template from the Pizza worksheet.

***

## Task 2 - Make the ball move

You just need one extra step:
* name the `something` and 
* make it move!

```python
# import libraries
from Tkinter import * 

# create the top level Tk object
window=Tk()
window.title("a pong")

# create the canvas
canvas = Canvas(window, height=600, width=600)

# draw stuff on the canvas
oval=canvas.create_oval(200,200,300,300,fill="brown")

# make it move
def move_oval(event=None):
    canvas.move(oval, 10, 10)
    canvas.after(100, move_oval)

move_oval()

# pack the canvas and run the Tk mainloop
canvas.pack()
window.mainloop()

```

The `after()` function calls the named function after 100ms. Moving things is easy as that!

***

## Task 3 - Running and saving your work

Files and IDEs allow you to save your work, and let you run it at the press of a key.

Remember to test and save your work after every change! If you are using Idle:

* click `<F5>` at the top left - did you get what you expected?
  * press this every time you want to see what your code does 
  * this should then appear in modal form labelled 'Tk'

* click `<Cntl-S>` - saved locally, no URL this time :/
  * the first time you will need to give a file name
  * save the file to a memory stick if you need to transport it

***

## Task 4 - Making a paddle

As Elly said, it's just a rectangle, this time moving with a keybinding.

```python
# import libraries
from Tkinter import * 

# create the top level Tk object
window=Tk()
window.title("a pong")

# create the canvas
canvas = Canvas(window, height=600, width=600)

# draw stuff on the canvas
rect=canvas.create_rectangle(100,100,150,200,fill="brown")

# make it move
def move_rect(event):
    canvas.move(rect, 0, 10)

window.bind("<Up>", move_rect)

# pack the canvas and run the Tk mainloop
canvas.pack()
window.mainloop()

```

All the keys on the keyboard can have keybindings; the special keys need `< >` the alphabetical keys are just in `" "`.

***

## Task 5 - What else does the Pong game need?

* bounce the ball off the edge
* move the paddle up & down
* make a goal & score card
* change the colours

***

## Task 6 - Can I make the ball bounce?

Bounces happen when things change direction, and go in the opposite direction with the same speed!

So, my ball needs to change direction when it gets to the edge - if on edge bounce - sounds familiar?

```python

# invariants
c_height,c_width=350,350
ballx, bally=0, 0
balldx, balldy=5, 5

def move_oval():
    # 'global' needed to stop python making a new thing
    # with the same name as the things outside
    # other languages work other way.
    # try removing these lines to see what happens.
    global ballx,bally
    global balldx,balldy

    if ballx<10 or ballx>c_width:
        balldx=-balldx

    if bally<10 or bally>c_height:
        balldy=-balldy

    ballx+=balldx
    bally+=balldy
    canvas.move(oval,balldx,balldy)
    canvas.after(100, move_oval)
```

Looks hard because I have to tell the computer ```exactly``` what to do.

Remember to remove the globals to see what happens - we are here to learn, not just to get the right answer.

***

## Task 7 - Can I stop the bat moving at the edge?

This one is easy, only allow the bat to move if it hasn't got to the edge yet!

```python
# invariants
baty=0

bat=canvas.create_rectangle(50,0,50,100)

def move_up(event):
    # remember why we need 'global'
    global baty
    baty-=10
    if baty>0:
       canvas.move(bat,0,-10)

def move_down(event):
    global baty
    baty+=10
    if bat<c_height-100:
       canvas.move(bat,0,10)
```

## Task 8 - Make the rest of the board?

We already know how to make rectangles and lines!

We know how to make text boxes - we just need to change the values we show.

Remember to make a scoring zone for the ball.


***

## Challenges

* jsfiddle & material design colours!
* an iPython notebook

***
