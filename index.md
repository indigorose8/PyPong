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
