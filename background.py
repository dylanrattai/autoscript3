from urllib import request
from datetime import *

currentDateP = datetime.now()
currentDate = currentDateP.strftime("%m-%d-%Y")

anchor1 = None
anchor2 = None

def exportSheet(): #this method of downloading will eventually become deprecated
    
    localFile = "./sheets/" + currentDate + "test.xlsx"
    request.urlretrieve("https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx", localFile)

def collectMain():
    from main import anchor1V, anchor2V
    global anchor1
    global anchor2
    anchor1 = str(anchor1V.get())
    anchor2 = str(anchor2V.get())