from tkinter import *
import pandas as pd #needs pip install
import background
from datetime import datetime

#main frames and root
root = Tk()
titleFrame = Frame(root)
underTitleFrame = Frame(root)
announcementBodyFrame = Frame(root)
infoFrame = Frame(root)
buttonFrame = Frame(root)
bodyFrame = Frame(root, bd=15)

#vars
announcementTitleV = "None"
posCurrent = 0
totalPos = 0
submitterV = "None"
submissionDateV = "None"
startDateV = "None"
endDateV = "None"
daysV = "None"
commentsV = "None"
bodyV = "None"

skipRows = None
sheetUnfiltered = pd.read_excel("./sheets/" + background.currentDate + ".xlsx", usecols="A, B, C, D, E, F, G, H")

def filterSheet():
    global skipRows
    for i in range(len(sheetUnfiltered.index)):
        if datetime.strptime(sheetUnfiltered.iat[i, "Start_Date"], "%m/%d/%Y") <= datetime.strptime(background.currentDate, "%m/%d/%Y") <= datetime.strptime(sheetUnfiltered.iat[i, "End_Date"], "%m/%d/%Y"):
            skipRows = i
            break

sheetFiltered = pd.read_excel("./sheets/" + background.currentDate + ".xlsx", nrows=skipRows, usecols="A, B, C, D, E, F, G, H")

#sub frames
submittedByFrame = Frame(infoFrame)
infoFrameTitleFrame = Frame(infoFrame)
subDateFrame = Frame(infoFrame)
startAirFrame = Frame(infoFrame)
endAirFrame = Frame(infoFrame)
displayDaysFrame = Frame(infoFrame)
commentsFrame = Frame(infoFrame)
backFrame = Frame(buttonFrame)
nextFrame = Frame(buttonFrame)
saveFrame = Frame(buttonFrame)
deleteFrame = Frame(buttonFrame)
copyFrame = Frame(buttonFrame)
printFrame = Frame(buttonFrame)

#window setting
root.title("Autoscript 3")
root.geometry("1000x800")
root.resizable(False, False)
screenWidth = root.winfo_reqwidth()
buttonDimensionW = int(screenWidth / 9 + 1)

#functions

def save():
    return "saved"

def next():
    global posCurrent
    if posCurrent < totalPos:
        posCurrent += 1
        refresh()

def last():
    global posCurrent
    if posCurrent > 0:
        posCurrent -= 1
    refresh()

def delete():
    #sheetUnfiltered.drop(posCurrent)
    sheetFiltered.drop(posCurrent)
    refresh()

def copy():
    return "copied"

def printSheet():
    return "printing"

def refresh():
    announcementTitleV = str(sheetFiltered.iat[posCurrent, "Announcement_Title"])
    submitterV = str(sheetFiltered.iat[posCurrent, "Your_Name"])
    submissionDateV = str(sheetFiltered.iat[posCurrent, "Timestamp"])
    startDateV = str(sheetFiltered.iat[posCurrent, "Start_Date"])
    endDateV = str(sheetFiltered.iat[posCurrent, "End_Date"])
    daysV = str(sheetFiltered.iat[posCurrent, "Days_Displayed"])
    commentsV = str(sheetFiltered.iat[posCurrent, "Comments"])
    bodyV = str(sheetFiltered.iat[posCurrent, "Announcement_Script"])

    announcementTitle.config(text=announcementTitleV)
    submitterFirst.config(text="(" + submitterV + ")")
    submitter.config(text=submitterV)
    submissionDate.config(text=submissionDateV)
    startAir.config(text=startDateV)
    endAir.config(text=endDateV)
    displayDays.config(text=daysV)
    comments.config(text=commentsV)
    body.config(text=bodyV)
    position.config(text="[" + str(posCurrent) + "/" + str(totalPos) + "]")

#declare all labels, buttons, etc then pack them
mainTitle = Label(titleFrame, text = "Autoscript 3", font=("Helvetica 45 bold"))
viewlast = Button(backFrame, text = "Back", command = last, width = buttonDimensionW)
viewNext = Button(nextFrame, text = "Next", command = next, width = buttonDimensionW)
saveButton = Button(saveFrame, text = "Save", command = save, width = buttonDimensionW)
deleteButton = Button(deleteFrame, text = "Delete", command = delete, width = buttonDimensionW)
copyButton = Button(copyFrame, text = "Copy", command = copy, width = buttonDimensionW)
printButton = Button(printFrame, text = "Print", command = printSheet, width = buttonDimensionW)
position = Label(underTitleFrame, text = "[" + str(posCurrent) + "/" + str(totalPos) + "]")
announcementTitle = Label(underTitleFrame, text = announcementTitleV)
submitter = Label(submittedByFrame, text = submitterV)
submitterFirst = Label(underTitleFrame, text = "(" + submitterV + ")")
submissionDate = Label(subDateFrame, text = submissionDateV)
startAir = Label(startAirFrame, text = startDateV)
endAir = Label(endAirFrame, text = endDateV)
displayDays = Label(displayDaysFrame, text = daysV)
submissionDateText = Label(subDateFrame, text = "Submission Date:", font='Helvetica 18 bold')
startAirText = Label(startAirFrame, text = "Start Date:", font='Helvetica 18 bold')
endAirText = Label(endAirFrame, text = "End Date:", font='Helvetica 18 bold')
displayDaysText = Label(displayDaysFrame, text = "Days Displayed:", font='Helvetica 18 bold')
submitterText = Label(submittedByFrame, text = "Submitted By:", font='Helvetica 18 bold')
infoText = Label(infoFrameTitleFrame, text = "Announcement Info", font='Helvetica 22 bold')
comments = Label(commentsFrame, text = commentsV)
commentsText = Label(commentsFrame, text = "Comments:", font='Helvetica 18 bold')
body = Label(bodyFrame, text=bodyV)

#pack more stuff
mainTitle.pack(side=TOP)
viewlast.pack()
viewNext.pack()
saveButton.pack()
deleteButton.pack()
copyButton.pack()
printButton.pack()
position.pack(side=LEFT)
announcementTitle.pack(side=LEFT)
submitter.pack(side=BOTTOM)
submitterFirst.pack(side=RIGHT)
submissionDate.pack(side=BOTTOM)
startAir.pack(side=BOTTOM)
endAir.pack(side=BOTTOM)
displayDaysText.pack(side=TOP)
displayDays.pack(side=BOTTOM)
submissionDateText.pack(side=TOP)
submissionDate.pack(side=BOTTOM)
startAirText.pack(side=TOP)
startAir.pack(side=BOTTOM)
endAirText.pack(side=TOP)
endAir.pack(side=BOTTOM)
displayDaysText.pack(side=TOP)
displayDays.pack(side=BOTTOM)
submitterText.pack(side=TOP)
submitterFirst.pack(side=BOTTOM)
infoText.pack(side=TOP)
comments.pack(side=BOTTOM)
commentsText.pack(side=TOP)
body.pack()

#pack all the sub frames
infoFrameTitleFrame.pack()
submittedByFrame.pack()
subDateFrame.pack()
startAirFrame.pack()
endAirFrame.pack()
displayDaysFrame.pack()
commentsFrame.pack()
backFrame.pack(side=LEFT)
nextFrame.pack(side=LEFT)
saveFrame.pack(side=LEFT)
deleteFrame.pack(side=LEFT)
copyFrame.pack(side=LEFT)
printFrame.pack(side=LEFT)

#pack the main frames
titleFrame.pack()
underTitleFrame.pack()
buttonFrame.pack(side=BOTTOM, anchor="w")
infoFrame.pack(side=LEFT, anchor="n")
bodyFrame.pack(anchor=NW)

root.mainloop()