from tkinter import *
import pandas as pd
import background
from datetime import datetime
import os
from win32 import win32print

#main frames and root
root = Tk()
root.config(bg="#031893")
titleFrame = Frame(root)
titleFrame.config(bg="#031893")
underTitleFrame = Frame(root)
underTitleFrame.config(bg="#031893")
announcementBodyFrame = Frame(root)
announcementBodyFrame.config(bg="#031893")
infoFrame = Frame(root)
infoFrame.config(bg="#031893")
buttonFrame = Frame(root)
buttonFrame.config(bg="#031893")
bodyFrame = Frame(root, bd = 15)
bodyFrame.config(bg="#031893")

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
printer = win32print.OpenPrinter("")# idk the printer

#stuff for filtering the sheet
skipRows = []
try:
    sheetUnfiltered = pd.read_excel(io = "./sheets/" + background.currentDate + ".xlsx", usecols = "A, B, C, D, E, F, G, H")

    for i in range(len(sheetUnfiltered.index)): #filter the sheet
        if datetime.strptime(sheetUnfiltered.iat[i, 3], "%m-%d-%Y") <= datetime.strptime(background.currentDate, "%m-%d-%Y") <= datetime.strptime(sheetUnfiltered.iat[i, 4], "%m-%d-%Y") and str(background.weekDay) in str(sheetUnfiltered.iat[i, 5]).lower():
            skipRows.append(i)

    sheetFiltered = pd.read_excel(io = "./sheets/" + background.currentDate + ".xlsx", skiprows = skipRows, usecols = "A, B, C, D, E, F, G, H")
    totalPos = len(skipRows)
except:
    print("Error in filtering sheet")
    
#sub frames
submittedByFrame = Frame(infoFrame)
submittedByFrame.config(bg="#031893")
infoFrameTitleFrame = Frame(infoFrame)
infoFrameTitleFrame.config(bg="#031893")
subDateFrame = Frame(infoFrame)
subDateFrame.config(bg="#031893")
startAirFrame = Frame(infoFrame)
startAirFrame.config(bg="#031893")
endAirFrame = Frame(infoFrame)
endAirFrame.config(bg="#031893")
displayDaysFrame = Frame(infoFrame)
displayDaysFrame.config(bg="#031893")
commentsFrame = Frame(infoFrame)
commentsFrame.config(bg="#031893")
backFrame = Frame(buttonFrame)
backFrame.config(bg="#031893")
nextFrame = Frame(buttonFrame)
nextFrame.config(bg="#031893")
saveFrame = Frame(buttonFrame)
saveFrame.config(bg="#031893")
deleteFrame = Frame(buttonFrame)
deleteFrame.config(bg="#031893")
copyFrame = Frame(buttonFrame)
copyFrame.config(bg="#031893")
printFrame = Frame(buttonFrame)
printFrame.config(bg="#031893")

#window setting
root.title("Autoscript 3")
root.geometry("1000x800")
root.resizable(False, False)
screenWidth = root.winfo_reqwidth()
buttonDimensionW = int(screenWidth / 9 + 1)

#functions
def save():
    try:
        sheetFiltered.to_excel(sheet_name = str(background.currentDate), mode = "a")
    except:
        print("Error in saving")
        
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
    try:
        sheetFiltered.drop(posCurrent)
        refresh()
    except:
        print("Error in deleting row")
        
def copy():
    return "copied"

def printSheet():
    try: #delete any old files that may have been made
        os.remove("./txt/" + background.currentDate + ".txt")
    except:
        print("Error in printing, Removing old file")
    try: #save to new txt
        with open("./txt/" + background.currentDate + ".txt", "w") as f:
            f.write(str(background.currentDate) + "Script\n\n")
            tmpV = 0
            for i in range(len(sheetFiltered)):
                if tmpV == 0:
                    f.write(str(background.anchor1) + ":\n" + str(sheetUnfiltered.iat[i, 6]))
                    tmpV = 1
                elif tmpV == 1:
                    f.write(str(background.anchor2) + ":\n" + str(sheetUnfiltered.iat[i, 6]))
                    tmpV = 0
            if background.weekDay == "monday":
                if tmpV == 0:
                    f.write(str(background.anchor1) + ":\n")
                    tmpV = 1
                elif tmpV == 1:
                    f.write(str(background.anchor2) + ":\n")
                    tmpV = 0
                f.write("And now for the pledge, \n I pledge allegiance to the flag of the United States of America, and to the republic for which it stands, one nation under God, indivisible, with liberty and justice for all.")
    except:
        print("Error in printing, Saving to txt")
    try:
        win32print.StartDocPrinter(printer, 1, ("test of raw data", None, "RAW"))
        win32print.StartPagePrinter(printer)
        win32print.WritePrinter(printer, "./txt/" + background.currentDate + ".txt")
        win32print.EndPagePrinter(printer)
    except:
        print("Error in printing, Printing")

def refresh():
    try:
        announcementTitleV = str(sheetFiltered.iat[posCurrent, "Announcement_Title"])
        submitterV = str(sheetFiltered.iat[posCurrent, "Your_Name"])
        submissionDateV = str(sheetFiltered.iat[posCurrent, "Timestamp"])
        startDateV = str(sheetFiltered.iat[posCurrent, "Start_Date"])
        endDateV = str(sheetFiltered.iat[posCurrent, "End_Date"])
        daysV = str(sheetFiltered.iat[posCurrent, "Days_Displayed"])
        commentsV = str(sheetFiltered.iat[posCurrent, "Comments"])
        bodyV = str(sheetFiltered.iat[posCurrent, "Announcement_Script"])
    except:
        print("Error in updating variables")
    
    try:
        announcementTitle.config(text = announcementTitleV)
        submitterFirst.config(text = "(" + submitterV + ")")
        submitter.config(text = submitterV)
        submissionDate.config(text = submissionDateV)
        startAir.config(text = startDateV)
        endAir.config(text = endDateV)
        displayDays.config(text = daysV)
        comments.config(text = commentsV)
        body.config(text = bodyV)
        position.config(text = "[" + str(posCurrent) + "/" + str(totalPos) + "]")
    except:
        print("Error in updating Labels")

#declare all labels, buttons, etc then pack them
mainTitle = Label(titleFrame, text = "Autoscript 3", font = ("Helvetica 45 bold"), bg="#031893", fg="white")
viewlast = Button(backFrame, text = "Back", command = last, width = buttonDimensionW, bg="#031893", fg="white", bd = 1)
viewNext = Button(nextFrame, text = "Next", command = next, width = buttonDimensionW, bg="#031893", fg="white", bd = 1)
saveButton = Button(saveFrame, text = "Save", command = save, width = buttonDimensionW, bg="#031893", fg="white", bd = 1)
deleteButton = Button(deleteFrame, text = "Delete", command = delete, width = buttonDimensionW, bg="#031893", fg="white", bd = 1)
copyButton = Button(copyFrame, text = "Copy", command = copy, width = buttonDimensionW, bg="#031893", fg="white", bd = 1)
printButton = Button(printFrame, text = "Print", command = printSheet, width = buttonDimensionW, bg="#031893", fg="white", bd = 1)
position = Label(underTitleFrame, text = "[" + str(posCurrent) + "/" + str(totalPos) + "]", bg="#031893", fg="white")
announcementTitle = Label(underTitleFrame, text = announcementTitleV, bg="#031893", fg="white")
submitter = Label(submittedByFrame, text = submitterV, bg="#031893", fg="white")
submitterFirst = Label(underTitleFrame, text = "(" + submitterV + ")", bg="#031893", fg="white")
submissionDate = Label(subDateFrame, text = submissionDateV, bg="#031893", fg="white")
startAir = Label(startAirFrame, text = startDateV, bg="#031893", fg="white")
endAir = Label(endAirFrame, text = endDateV, bg="#031893", fg="white")
displayDays = Label(displayDaysFrame, text = daysV, bg="#031893", fg="white")
submissionDateText = Label(subDateFrame, text = "Submission Date:", font = "Helvetica 18 bold", bg="#031893", fg="white")
startAirText = Label(startAirFrame, text = "Start Date:", font = "Helvetica 18 bold", bg="#031893", fg="white")
endAirText = Label(endAirFrame, text = "End Date:", font = "Helvetica 18 bold", bg="#031893", fg="white")
displayDaysText = Label(displayDaysFrame, text = "Days Displayed:", font = "Helvetica 18 bold", bg="#031893", fg="white")
submitterText = Label(submittedByFrame, text = "Submitted By:", font = "Helvetica 18 bold", bg="#031893", fg="white")
infoText = Label(infoFrameTitleFrame, text = "Announcement Info", font = "Helvetica 22 bold", bg="#031893", fg="white")
comments = Label(commentsFrame, text = commentsV, bg="#031893", fg="white")
commentsText = Label(commentsFrame, text = "Comments:", font = 'Helvetica 18 bold', bg="#031893", fg="white")
#body = Text(bodyFrame, text = bodyV, bg="#031893", fg="white")
body = Text(bodyFrame, height = 500, width = 250, bg="#031893", fg="white", bd = 0)

#pack more stuff
mainTitle.pack(side = TOP)
viewlast.pack()
viewNext.pack()
saveButton.pack()
deleteButton.pack()
copyButton.pack()
printButton.pack()
position.pack(side = LEFT)
announcementTitle.pack(side = LEFT)
submitter.pack(side = BOTTOM)
submitterFirst.pack(side = RIGHT)
submissionDate.pack(side = BOTTOM)
startAir.pack(side = BOTTOM)
endAir.pack(side = BOTTOM)
displayDaysText.pack(side = TOP)
displayDays.pack(side = BOTTOM)
submissionDateText.pack(side = TOP)
submissionDate.pack(side = BOTTOM)
startAirText.pack(side = TOP)
startAir.pack(side = BOTTOM)
endAirText.pack(side = TOP)
endAir.pack(side = BOTTOM)
displayDaysText.pack(side = TOP)
displayDays.pack(side = BOTTOM)
submitterText.pack(side = TOP)
submitterFirst.pack(side = BOTTOM)
infoText.pack(side = TOP)
comments.pack(side = BOTTOM)
commentsText.pack(side = TOP)
body.pack()

#pack all the sub frames
infoFrameTitleFrame.pack()
submittedByFrame.pack()
subDateFrame.pack()
startAirFrame.pack()
endAirFrame.pack()
displayDaysFrame.pack()
commentsFrame.pack()
backFrame.pack(side = LEFT)
nextFrame.pack(side = LEFT)
saveFrame.pack(side = LEFT)
deleteFrame.pack(side = LEFT)
copyFrame.pack(side = LEFT)
printFrame.pack(side = LEFT)

#pack the main frames
titleFrame.pack()
underTitleFrame.pack()
buttonFrame.pack(side = BOTTOM, anchor = W)
infoFrame.pack(side = LEFT, anchor = N)
bodyFrame.pack(anchor = NW)

root.mainloop()