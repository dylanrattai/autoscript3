from tkinter import *
import pandas as pd #needs pip install
import background

#main frames and root
root = Tk()
titleFrame = Frame(root)
underTitleFrame = Frame(root)
announcementBodyFrame = Frame(root)
infoFrame = Frame(root)
buttonFrame = Frame(root)

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
sheetUnfiltered = pd.read_excel("./sheets/" + background.currentDate + ".xlsx", usecols="B, C, D, E, F, G, H")
#sheetFiltered = pd.read_excel("./sheets/" + background.currentDate + ".xlsx", nrows=skipRows, usecols="A, B, C, D, E, F, G, H")

screenWidth = root.winfo_reqwidth()
buttonDimensionW = int(screenWidth / 9 + 1) #it isnt exactly right on the print button :/

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

#functions
def filterSheet():
    global skipRows

def save():
    return "saved"

def next():
    global posCurrent
    posCurrent += 1
    refresh()

def last():
    global posCurrent
    if posCurrent > 0:
        posCurrent -= 1
    refresh()

def delete():
    return "deleted"

def copy():
    return "copied"

def printSheet():
    return "printing"

def refresh():
    announcementTitleV = str(pd.iat[posCurrent, "Announcement_Title"])
    submitterV = str(pd.iat[posCurrent, "Your_Name"])
    submissionDateV = str(pd.iat[posCurrent, "Timestamp"])
    startDateV = str(pd.iat[posCurrent, "Start_Date"])
    endDateV = str(pd.iat[posCurrent, "End_Date"])
    daysV = str(pd.iat[posCurrent, "Days_Displayed"])
    commentsV = str(pd.iat[posCurrent, "Comments"])
    bodyV = str(pd.iat[posCurrent, "Announcement_Script"])

    announcementTitle.config(text=announcementTitleV)
    submitterFirst.config(text=submitterV)
    submitter.config(text=submitterV)
    submissionDate.config(text=submissionDateV)
    startAir.config(text=startDateV)
    endAir.config(text=endDateV)
    displayDays.config(text=daysV)
    comments.config(text=commentsV)
    #body.config(text=bodyV)
    position.config(text="[" + str(posCurrent) + "/" + str(totalPos) + "]")

#declare all labels, buttons, etc then pack them
mainTitle = Label(titleFrame, text = "Autoscript 3", font=("Helvetica 45 bold")).pack(side=TOP)
viewlast = Button(backFrame, text = "Back", command = last, width = buttonDimensionW).pack()
viewNext = Button(nextFrame, text = "Next", command = next, width = buttonDimensionW).pack()
saveButton = Button(saveFrame, text = "Save", command = save, width = buttonDimensionW).pack()
deleteButton = Button(deleteFrame, text = "Delete", command = delete, width = buttonDimensionW).pack()
copyButton = Button(copyFrame, text = "Copy", command = copy, width = buttonDimensionW).pack()
printButton = Button(printFrame, text = "Print", command = printSheet, width = buttonDimensionW).pack()
position = Label(underTitleFrame, text = "[" + str(posCurrent) + "/" + str(totalPos) + "]").pack(side=LEFT)
announcementTitle = Label(underTitleFrame, text = announcementTitleV).pack(side=LEFT)
submitter = Label(submittedByFrame, text = submitterV).pack(side=BOTTOM)
submitterFirst = Label(underTitleFrame, text = "(" + submitterV + ")").pack(side=RIGHT)
submissionDate = Label(subDateFrame, text = submissionDateV).pack(side=BOTTOM)
startAir = Label(startAirFrame, text = startDateV).pack(side=BOTTOM)
endAir = Label(endAirFrame, text = endDateV).pack(side=BOTTOM)
displayDays = Label(displayDaysFrame, text = daysV).pack(side=BOTTOM)
submissionDateText = Label(subDateFrame, text = "Submission Date:", font='Helvetica 18 bold').pack(side=TOP)
startAirText = Label(startAirFrame, text = "Start Date:", font='Helvetica 18 bold').pack(side=TOP)
endAirText = Label(endAirFrame, text = "End Date:", font='Helvetica 18 bold').pack(side=TOP)
displayDaysText = Label(displayDaysFrame, text = "Days Displayed:", font='Helvetica 18 bold').pack(side=TOP)
submitterText = Label(submittedByFrame, text = "Submitted By:", font='Helvetica 18 bold').pack(side=TOP)
infoText = Label(infoFrameTitleFrame, text = "Announcement Info", font='Helvetica 22 bold').pack(side=TOP)
comments = Label(commentsFrame, text = commentsV).pack(side=BOTTOM)
commentsText = Label(commentsFrame, text = "Comments:", font='Helvetica 18 bold').pack(side=TOP)

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

root.mainloop()