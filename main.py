from tkinter import *
from subprocess import call
import background

versionNum = "Version 1.0 "

root = Tk()

anchor1V = StringVar()
anchor2V = StringVar()

#functions
def done():
    background.exportSheet()
    root.destroy()
    call(["python", "index.py"])
    #background.collectMain()

#window settings
root.title("Autoscript 3")
root.geometry("800x400")
root.resizable(False, False)

#set all frames
titleFrame = Frame(root)
anchorsFrame = Frame(root)
anchorsFrame1 = Frame(anchorsFrame)
anchorsFrame2 = Frame(anchorsFrame)
doneFrame = Frame(root)
verFrame = Frame(root)

#declare all labels, buttons, etc
blank = Label(doneFrame, text = "   ").pack(side=BOTTOM)
mainTitle = Label(titleFrame, text = "Autoscript 3\n", font="Helvetica 45 bold").pack(side=TOP)
anchor1 = Label(anchorsFrame1, text = "Anchor 1:  ", font="Helvetica 15").pack(side=LEFT)
anchor2 = Label(anchorsFrame2, text = "Anchor 2:  ", font="Helvetica 15").pack(side=LEFT)
doneButton = Button(doneFrame, text = "Done", font="Helvetica 15", command = done).pack(side=TOP)
#sheetLink = Label(, text = "Google Sheets File")
inputAnchor1 = Entry(anchorsFrame1,textvariable=anchor1V).pack(side=LEFT)
inputAnchor2 = Entry(anchorsFrame2,textvariable=anchor2V).pack(side=LEFT)
#inputSheetLink = Entry()
verNum = Label(verFrame, text = versionNum).pack()

#pack frames
anchorsFrame1.pack(side=TOP)
anchorsFrame2.pack(side=BOTTOM)
titleFrame.pack()
anchorsFrame.pack()
verFrame.pack(side=BOTTOM, anchor="e")
doneFrame.pack(side=BOTTOM)

root.mainloop()