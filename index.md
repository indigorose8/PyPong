#Python Pong worksheet

##Task 1 - Move that ball

Remember the steps in making a minimal  tk canvas:
             
```python
        #import the libraries
        #create a top level object
        #attach a canvas
        #draw something
        #run the mainloop
```

Can you spot the extra step - to name the `something` and make it move!

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

***

##Task 2 - Running and saving your work

Files and IDEs allow you to save your work, and let you run it at the press of a key.

Remember to test and save your work after every change!

* click *run* at the top left - did you get what you expected?
  * press this every time you want to see what your code does 
  * this should then appear in modal form labelled 'Tk'

* click *save* at the top left - no URL this time :/
  * the first time you will need to give a file name
  * save the file to a memory stick if you need to transport it

***

##Task 3 - Making a paddle

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

***

##Task 4 - What else do the balls and paddle need to do?

*move the paddle up & down
*bounce the ball of the paddle
*make a goal

***

##Task 5 - Can I make a web version?

jsfiddle & material design colours!

***
