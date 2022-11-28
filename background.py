from urllib import request
from datetime import *
import wget
import os

currentDateP = datetime.now()
currentDate = currentDateP.strftime("%m-%d-%Y")
# 0 = Mon, 1 = Tues, 2 = Wed, 3 = Thurs, 4 = Fri, 5 = Sat, 6 = Sun
weekDay = datetime.weekday()

if weekDay == 0:
    weekDay = "monday"
elif weekDay == 1:
    weekDay = "tuesday"
elif weekDay == 2:
    weekDay = "wednesday"
elif weekDay = 3:
    weekDay = "thursday"
elif weekDay == 4:
    weekDay = "friday"

anchor1 = None
anchor2 = None

def exportSheet():
    localFile = "./sheets/" + currentDate + ".xlsx"
    if os.path.exists("./sheets/" + currentDate + ".xlsx"):
        print("File already downloaded")
    else:
        #request.urlretrieve("https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx", localFile)
        wget.download("https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx", localFile)