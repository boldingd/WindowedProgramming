#! /usr/bin/python3

import tkinter

def pr_clicked():
    print("named function callbaq")

class basic(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        l = tkinter.Label(self, text="A Label")
        l.grid(row=0, column=0)

        b = tkinter.Button(self, text="A Button", command=lambda: print("cliqued"))
        b.grid(row=1, column=0)

        b2 = tkinter.Button(self, text="Another Button", command=pr_clicked)
        b2.grid(row=2, column=0)

if __name__ == "__main__":
    root = tkinter.Tk()
    b = basic(root)
    b.pack()
    root.mainloop()
