from tkinter import *

root = Tk()

blank = Label(root, text = "   ")
mainTitle = Label(root, text = "Autoscript 3\n", font=("Impact, 32"))
viewlast = Label(root, text = "Back")
viewNext = Label(root, text = "Next")
saveButton = Label(root, text = "Save")
deleteButton = Label(root, text = "Delete")
copyButton = Label(root, text = "Copy")
printButton = Label(root, text = "Print")

mainTitle.grid(row=1, column=0)

root.mainloop()
