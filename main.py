from tkinter import *
from subprocess import call
import background
import os

versionNum = "Version 1.0 "
root = Tk()

#functions
def done():
    background.anchor1 = inputAnchor1.get()
    background.anchor2 = inputAnchor2.get()
    background.exportSheet()
    root.destroy()
    call(["python", "index.py"])

def clear():
    dir = './sheets/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    dir2 = './txt/'
    for f in os.listdir(dir2):
        os.remove(os.path.join(dir2, f))

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
blank = Label(doneFrame, text = "                   ", bg="#031893", bd = 0).pack(side=BOTTOM)
mainTitle = Label(titleFrame, text = "Autoscript 3\n", font="Helvetica 45 bold", bg="#031893", fg="white").pack(side=TOP)
anchor1 = Label(anchorsFrame1, text = "Anchor 1:  ", font="Helvetica 15", bg="#031893", fg="white").pack(side=LEFT)
anchor2 = Label(anchorsFrame2, text = "Anchor 2:  ", font="Helvetica 15", bg="#031893", fg="white").pack(side=LEFT)
doneButton = Button(doneFrame, text = "Done", font="Helvetica 15", command = done, bg="#031893", fg="white", bd = 0).pack(side=TOP)
inputAnchor1 = Entry(anchorsFrame1, bd = 0)
inputAnchor2 = Entry(anchorsFrame2, bd = 0)
verNum = Label(verFrame, text = versionNum, bg="#031893", fg="white").pack()
root.config(bg="#031893")
verFrame.config(bg="#031893")
anchorsFrame1.config(bg="#031893")
anchorsFrame2.config(bg="#031893")
clearButton = Button(verFrame, text = "Clear Folders", bg="#031893", fg="white", command = clear, bd = 0)

#pack frames
anchorsFrame1.pack(side=TOP)
anchorsFrame2.pack(side=BOTTOM)
titleFrame.pack()
anchorsFrame.pack()
verFrame.pack(side=BOTTOM, anchor=E)
clearButton.pack(side=TOP, anchor=E)
doneFrame.pack(side=BOTTOM)
inputAnchor1.pack(side=LEFT)
inputAnchor2.pack(side=LEFT)

root.mainloop()