from re import sub
from tkinter import *

root = Tk()

def save():
    return "saved"

def next():
    return "next"

def last():
    return "last"

def delete():
    return "deleted"

def copy():
    return "copied"

def print():
    return "printing"

blank = Label(root, text = "   ")
mainTitle = Label(root, text = "Autoscript 3\n", font=("Impact, 32"))
viewlast = Button(root, text = "Back", command = last())
viewNext = Button(root, text = "Next", command = next())
saveButton = Button(root, text = "Save", command = save())
deleteButton = Button(root, text = "Delete", command = delete())
copyButton = Button(root, text = "Copy", command = copy())
printButton = Button(root, text = "Print", command = print())
announcementTitle = Label(root, text = "Add variable here")
position = Label(root, text = "[" + "Add variable here" + "/" + "Add variable here" + "]")
submitter = Label(root, text = "Add variable here")
submitterFirst = Label(root, text = "(" + "Add variable here" + ")")
submissionDate = Label(root, text = "Add variable here")
startAir = Label(root, text = "Add variable here")
endAir = Label(root, text = "Add variable here")
displayDays = Label(root, text = "Add variable here")
submissionDateText = Label(root, text = "Submission Date:", font='Helvetica 18 bold')
startAirText = Label(root, text = "Add variable here", font='Helvetica 18 bold')
endAirText = Label(root, text = "Add variable here", font='Helvetica 18 bold')
displayDaysText = Label(root, text = "Add variable here", font='Helvetica 18 bold')
submitterText = Label(root, "Submitted By", font='Helvetica 18 bold')

root.mainloop()