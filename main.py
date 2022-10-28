from tkinter import *

versionNum = "Version 1.0 "

root = Tk()

#functions
def done():
    root.destroy()

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
blank = Label(doneFrame, text = "   ")
mainTitle = Label(titleFrame, text = "Autoscript 3\n", font="Helvetica 45 bold")
anchor1 = Label(anchorsFrame1, text = "Anchor 1:  ", font="Helvetica 15")
anchor2 = Label(anchorsFrame2, text = "Anchor 2:  ", font="Helvetica 15")
doneButton = Button(doneFrame, text = "Done", font="Helvetica 15", command = done(), activebackground = "black")
#sheetLink = Label(, text = "Google Sheets File")
inputAnchor1 = Entry(anchorsFrame1)
inputAnchor2 = Entry(anchorsFrame2)
#inputSheetLink = Entry()
verNum = Label(verFrame, text = str(versionNum))

#pack everything
anchorsFrame1.pack(side=TOP)
anchorsFrame2.pack(side=BOTTOM)
mainTitle.pack(side=TOP)
#sheetLink.pack(row=2, column=0)
#inputSheetLink.pack(row=2, column=1)
anchor1.pack(side=LEFT)
inputAnchor1.pack(side=LEFT)
anchor2.pack(side=LEFT)
inputAnchor2.pack(side=LEFT)
doneButton.pack(side=TOP)
blank.pack(side=BOTTOM)
titleFrame.pack()
anchorsFrame.pack()
verFrame.pack(side=BOTTOM, anchor="e")
doneFrame.pack(side=BOTTOM)
verNum.pack()

root.mainloop()