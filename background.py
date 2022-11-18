from urllib import request
from datetime import *
#import wget #needs pip install

currentDateP = datetime.now()
currentDate = currentDateP.strftime("%m-%d-%Y")

anchor1 = None
anchor2 = None

def exportSheet(): #this method of downloading will eventually become deprecated
    print(anchor1)
    print(anchor2)
    localFile = "./sheets/" + currentDate + "test.xlsx"
    #request.urlretrieve("https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx", localFile)
    #wget.download("https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx", localFile)