from tkinter import *

root = Tk()

def done():
    return done

blank = Label(root, text = "   ")
mainTitle = Label(root, text = "Autoscript 3\n", font=("Impact, 32"))
anchor1 = Label(root, text = "Anchor 1:")
anchor2 = Label(root, text = "Anchor 2:")
doneButton = Button(root, text = "Done", command = done)
inputAnchor1 = Entry(root)
inputAnchor2 = Entry(root)

mainTitle.grid(row=1, column=0)
anchor1.grid(row=3, column=0)
inputAnchor1.grid(row=3, column=1)
anchor2.grid(row=4, column=0)
inputAnchor2.grid(row=4, column=1)
blank.grid(row=5, column=0)
doneButton.grid(row=6, column=0)

root.mainloop()