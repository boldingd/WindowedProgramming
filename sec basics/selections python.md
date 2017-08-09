Selection Widgets in Python
===========================

Now let's look at selection widgets using Python and Tk.
Tk exposes the state of controls like check-boxes by linking themseves to an external variable, which they update when their state changes.
It expects these variables to be instances of one of several "`Var` classes", included in the tkinter package.
A `Var` class "wraps" a normal python object; we can get get or set the state of that object using the `get` and `set` methods.

## Starting Out

We'll create a new class inheriting from `tkinter.Frame`.
(Unlike Java, Python doesn't require us to place each class in its own file; we can create a new file for our class, or place our class in the existing file from last time.
If we create a new file for our class, we'll have to `import` that file -- with, for example `import checks` if we created our new widget in `checks.py`.)

In either case, we'll start by creating a class that inherits from `tkinter.Frame`; then, we'll add a `tkinter. IntVar`, and create a `tkinter.Checkbox` linked to it:

``` python
import tkinter

class checks(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self._checked = tkinter.IntVar()

        cb = tkinter.Checkbutton(self, text="Check Me", variable=self._checked)
        cb.grid(row=0, column=0)
```

`IntVar` is the type of "tkinter variabl class" that the Checkbox expects.
Notice that we stored a reference to the `IntVar` in the class, but we didn't store a reference to the `Checkbox` *itself*; that is because, for this simple example, we only anticipate needing to know if the `Checkbox` is checked or not, and we only need the `_checked` `IntVar` for that.
(Of course, we *could* also store a reference to the Checkbox if we wanted to.)

Often, we only care about the state of the check-box when some other action occurs - like when a submit button is clicked.
We can, however, specify a command for the check-box itself:

``` python
import tkinter

class checks(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self._checked = tkinter.IntVar()

        cb = tkinter.Checkbutton(self, text="Check Me", variable=self._checked, command=self.__cb_callback)
        cb.grid(row=0, column=0)

    def __cb_callback(self):
        print("callback state:  {}".format(self._checked.get()))
```

## Radio Buttons

To add a group of radio buttons, we first need to create a `tkinter.StringVar`, and then provide that as a variable to the `tkinter.Checkbox` constructor:

``` python
        self._g1_selection = tkinter.StringVar()

        rb_g1_1 = tkinter.Radiobutton(self, text="Option 1", variable=self._g1_selection, value="1")
        rb_g1_1.grid(row=1, column=1)

        rb_g1_2 = tkinter.Radiobutton(self, text="Option 2", variable=self._g1_selection, value="2")
        rb_g1_2.grid(row=2, column=1)
```

As before, we could also provide callbacks (with the `command` named-parameter) for the radio-buttons themselves, but we are usually only concerned with the current selection, and the `_selection` `Stringvar` will give us that information.
We *might* want to know when the selection changes; to do this, we *might* specify a `command` for each radio button in the group.
TK, however, provides us a better way: we can provide a function *to the StringVar*, which it will call when it's value changes (or when it is *read*, or when the `StringVar` is deleted).

``` python
        self._g1_selection.trace("w", lambda *args: print(self._g1_selection.get()) )
```

Here, `w` is the *mode*; it should be `w` if we want our command to be called when the variable is *written* - which is the case that we care about here - or `r` if we want to be notified when the variable is read, or `u` for when the variable is deleted.
(We used `*args` in the lambda to collect all the arguments to the command, since in this case we don't particularly care what they were.)

If we want to create a second group, we can do that by specifying a different `tkinter.Stringvar`:

``` python
        self._g2_selection = tkinter.StringVar()

        rb_g2_1 = tkinter.Radiobutton(self, text="Option A", variable=self._g2_selection, value="A")
        rb_g2_1.grid(row=1, column=2)

        rb_g2_2 = tkinter.Radiobutton(self, text="Option B", variable=self._g2_selection, value="B")
        rb_g2_2.grid(row=2, column=2)
```

Notice that we've also changed the column value; this will lay out these radio buttons next to the radio buttons from the first group.

## Combo Boxes

The `tkinter` package itself does not include a combo-box widget; however, the `tkinter.ttk` sub-package does.
(The `tkinter.ttk` package provides support for *themed* tk widgets; it includes several new widgets, and it includes replacements for existing `Tk` widgets that include *theming* support.)

Once we import the `tkinter.ttk` package, we can create a `StringVar`, and construct a combo-box linked to it:

``` python
        self._combo_selection = tkinter.StringVar()

        combo = tkinter.ttk.Combobox(self, textvariable=self._combo_selection)
        combo['values'] = ("Option A", "Option B", "Option C")

        combo.grid(row=3, column=0)
```

The user will be able to type a value into this combo-box; this might not be what we want.
If we want to restrict the user to only the values that we have provided, we can add "readonly" to the combo-box's state:

``` python
        combo.state(['readonly'])
```

If we want to be alerted when the combo-box is changed, we could *trace* the `self._combo_selection` variable the way we did before, or we can *bind* a callback to the combo-box's `ComboboxSelected` event.
(This is one of Tk's two event-handling systems: specifying commands is the other one.)
We can use `bind` like this:

``` python
        combo.bind('<<ComboboxSelected>>', lambda event: print(self._combo_selection.get()))
```
