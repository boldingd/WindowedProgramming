First Steps: Displays, Controls and Layouts
===========================================

Let's build a simple layout in python3, using Tk.

We'll start by importing the TK library itself:

    import tkinter as tk

...we can then create a *root window* that will contain our interface:

    rw = tk.Tk()

... and we can then create a label:

    l = tk.Label(rw, text="a label")

Notice that we gave the *parent* of the button -- in this case, the root window -- as the first parameter to the label's constructor.

We also need to tell the system *where* this label should be placed -- or it won't show up when we run the program!
In the simplest case, we can do this with the `pack()` method.

    l.pack()`

Finally, we can start the event-processing loop, so that our application will actually run:

    rw.mainloop()

The `pack` is a component of one of two layout systems provided by Tk.
Pack places a widget in one of five locations -- the top, left, bottom or right edge, or in the center.
(If we call `pack` without any argument, it will place the widget against the top edge.)
Though `pack` is simple, it's also very limited -- so much so that its primary use is likely in teaching examples!

## Buttons and Grids

Let's add a button, and let's use the more sophisticated `grid` system.
Grid allows us to specify a row and column coordinate (the zeroth-row and zeroth-column is at the top-left corner of the window).

```import tkinter as tk

rw = tk.Tk()

l = tk.Label(rw, text="a label")
l.grid(row=0, column=0)

b = tk.Button(rw, text="a button")
b.grid(row=1, column=0)

rw.mainloop()```

A button that doesn't do anything isn't much use; let's assign an action to it.
First we'll define a function, and then we'll assign it as the button's callback.

```def b_clicked():
    print("clicked")

b = tk.Button(rw, text="a button", command=b_clicked)```

Notice that we're using the name of a function as if it were a *value*; this is a feature of python (and some other languages) that some readers might not be familiar with.
Python also allows us a slightly more compact syntax, that allows us to declare an *anonymous* function *in-line*:

    b = tk.Button(rw, text="a button", command=lambda: print("clicked"))

(Note that lambda expressions must be exactly one statement.)

## Wrapping our widget in a class

This works, but we would generally like our interfaces to be more self-contained.
Let's wrap our interface inside a class.
Our class needs to be a *widget* itself, so that we can use it in layouts like other widgets.

```import tkinter as tk

class Basic(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        l = tk.Label(self, text="a label")
        l.grid(row=0, column=0)

        b = tk.Button(self, text="A Button", command=lambda: print("clicked"))
        b.grid(row=1, column=0)

root = tk.Tk()
b = Basic(root)
b.pack()
root.mainloop()```

We use tk.Frame as the parent class.
Frame is a *container widget*, designed to contain child widgets and lay them out; it makes a good parent class for our widget.
Notice that the constructor takes a single parameter, `parent`, which we pass into our superclass's constructor; this is necessary to make sure that our widget is set up correctly.
(Python, unlike some other languages, does not automatically call superclass constructors; if we want instances of our class to be set up the way a Frame would be, we have to call the Frame's constructor ourselves.)
Notice also that, as we construct our layout, we still pass the parent widget into each widget's constructor as the first argument -- only now that parent is `self`, the widget that we are buliding.

With all of this in place, we can use our Basic widget exactly like any other widget!