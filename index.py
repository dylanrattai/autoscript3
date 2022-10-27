from tkinter import *

root = Tk()
titleFrame = Frame(root)
underTitleFrame = Frame(root)
announcementBodyFrame = Frame(root)
infoFrame = Frame(root)
buttonFrame = Frame(root)

submittedByFrame = Frame(infoFrame)
infoFrameTitleFrame = Frame(infoFrame)

root.title("Autoscript 3")
root.geometry("1000x800")

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

mainTitle = Label(titleFrame, text = "Autoscript 3\n", font=("Helvetica 45 bold"))
#viewlast = Button(root, text = "Back", command = last())
#viewNext = Button(root, text = "Next", command = next())
#saveButton = Button(root, text = "Save", command = save())
#deleteButton = Button(root, text = "Delete", command = delete())
#copyButton = Button(root, text = "Copy", command = copy())
#printButton = Button(root, text = "Print", command = print())
announcementTitle = Label(underTitleFrame, text = "Add variable here")
position = Label(underTitleFrame, text = "[" + "Add variable here" + "/" + "Add variable here" + "]")
submitter = Label(submittedByFrame, text = "Add variable here")
submitterFirst = Label(underTitleFrame, text = "(" + "Add variable here" + ")")
#submissionDate = Label(root, text = "Add variable here")
#startAir = Label(root, text = "Add variable here")
#endAir = Label(root, text = "Add variable here")
#displayDays = Label(root, text = "Add variable here")
#submissionDateText = Label(root, text = "Submission Date:", font='Helvetica 18 bold')
#startAirText = Label(root, text = "Add variable here", font='Helvetica 18 bold')
#endAirText = Label(root, text = "Add variable here", font='Helvetica 18 bold')
#displayDaysText = Label(root, text = "Add variable here", font='Helvetica 18 bold')
submitterText = Label(submittedByFrame, text = "Submitted By", font='Helvetica 18 bold')
infoText = Label(infoFrameTitleFrame, text = "Announcement Info", font='Helvetica 22 bold')

mainTitle.pack(side=TOP)
position.pack(side=LEFT)
announcementTitle.pack(side=LEFT)
submitterFirst.pack(side=RIGHT)
submitter.pack(side=BOTTOM)
submitterText.pack(side=TOP)
infoText.pack(side=TOP)

infoFrameTitleFrame.pack(side=TOP)
submittedByFrame.pack(side=TOP)

titleFrame.pack()
underTitleFrame.pack()
infoFrame.pack(side=LEFT)

root.mainloop()