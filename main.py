from tarfile import PAX_FIELDS
from tkinter import *

root = Tk()

def done():
    return done

root.title("Autoscript 3")
root.geometry("800x400")

titleFrame = Frame(root)
anchorsFrame = Frame(root)
anchorsFrame1 = Frame(anchorsFrame)
anchorsFrame2 = Frame(anchorsFrame)
doneFrame = Frame(root)

blank = Label(doneFrame, text = "   ")
mainTitle = Label(titleFrame, text = "Autoscript 3\n", font="Helvetica 45 bold")
anchor1 = Label(anchorsFrame1, text = "Anchor 1:  ", font="Helvetica 15")
anchor2 = Label(anchorsFrame2, text = "Anchor 2:  ", font="Helvetica 15")
doneButton = Button(doneFrame, text = "Done", font="Helvetica 15", command = done(), activebackground = "black")
sheetLink = Label(root, text = "Google Sheets File")
inputAnchor1 = Entry(anchorsFrame1)
inputAnchor2 = Entry(anchorsFrame2)
inputSheetLink = Entry(root)

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
anchorsFrame.pack(padx=10)
doneFrame.pack(side=BOTTOM)

root.mainloop()