from tkinter import *

#main frames and root
root = Tk()
titleFrame = Frame(root).pack()
underTitleFrame = Frame(root).pack()
buttonFrame = Frame(root).pack(side=BOTTOM, anchor="w")
announcementBodyFrame = Frame(root)
infoFrame = Frame(root).pack(side=LEFT, anchor="n")

#vars
screenWidth = root.winfo_reqwidth()
screenHeight = root.winfo_reqheight()
buttonDimensionW = int(screenWidth / 9 + 1) #it isnt exactly right on the print button :/

#sub frames
infoFrameTitleFrame = Frame(infoFrame).pack()
submittedByFrame = Frame(infoFrame).pack()
subDateFrame = Frame(infoFrame).pack()
startAirFrame = Frame(infoFrame).pack()
endAirFrame = Frame(infoFrame).pack()
displayDaysFrame = Frame(infoFrame).pack()
commentsFrame = Frame(infoFrame).pack()
backFrame = Frame(buttonFrame).pack(side=LEFT)
nextFrame = Frame(buttonFrame).pack(side=LEFT)
saveFrame = Frame(buttonFrame).pack(side=LEFT)
deleteFrame = Frame(buttonFrame).pack(side=LEFT)
copyFrame = Frame(buttonFrame).pack(side=LEFT)
printFrame = Frame(buttonFrame).pack(side=LEFT)

#window setting
root.title("Autoscript 3")
root.geometry("1000x800")
root.resizable(False, False)

#functions for buttons
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

#declare all labels, buttons, etc then pack them
mainTitle = Label(titleFrame, text = "Autoscript 3\n", font=("Helvetica 45 bold")).pack(side=TOP)
viewlast = Button(backFrame, text = "Back", command = last(), width = buttonDimensionW).pack()
viewNext = Button(nextFrame, text = "Next", command = next(), width = buttonDimensionW).pack()
saveButton = Button(saveFrame, text = "Save", command = save(), width = buttonDimensionW).pack()
deleteButton = Button(deleteFrame, text = "Delete", command = delete(), width = buttonDimensionW).pack()
copyButton = Button(copyFrame, text = "Copy", command = copy(), width = buttonDimensionW).pack()
printButton = Button(printFrame, text = "Print", command = print(), width = buttonDimensionW).pack()
announcementTitle = Label(underTitleFrame, text = "Add variable here").pack(side=LEFT)
position = Label(underTitleFrame, text = "[" + "Add variable here" + "/" + "Add variable here" + "]").pack(side=LEFT)
submitter = Label(submittedByFrame, text = "Add variable here").pack(side=BOTTOM)
submitterFirst = Label(underTitleFrame, text = "(" + "Add variable here" + ")").pack(side=RIGHT)
submissionDate = Label(subDateFrame, text = "Add variable here").pack(side=BOTTOM)
startAir = Label(startAirFrame, text = "Add variable here").pack(side=BOTTOM)
endAir = Label(endAirFrame, text = "Add variable here").pack(side=BOTTOM)
displayDays = Label(displayDaysFrame, text = "Add variable here").pack(side=BOTTOM)
submissionDateText = Label(subDateFrame, text = "Submission Date:", font='Helvetica 18 bold').pack(side=TOP)
startAirText = Label(startAirFrame, text = "Start Date:", font='Helvetica 18 bold').pack(side=TOP)
endAirText = Label(endAirFrame, text = "End Date:", font='Helvetica 18 bold').pack(side=TOP)
displayDaysText = Label(displayDaysFrame, text = "Days Displayed:", font='Helvetica 18 bold').pack(side=TOP)
submitterText = Label(submittedByFrame, text = "Submitted By:", font='Helvetica 18 bold').pack(side=TOP)
infoText = Label(infoFrameTitleFrame, text = "Announcement Info", font='Helvetica 22 bold').pack(side=TOP)
comments = Label(commentsFrame, text="Add Variable Here").pack(side=BOTTOM)
commentsText = Label(commentsFrame, text = "Comments:", font='Helvetica 18 bold').pack(side=TOP)

root.mainloop()