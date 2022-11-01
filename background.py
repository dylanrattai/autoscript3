import requests

#             test spreadsheet
urls = ["https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx"]
anchor1 = None
anchor2 = None

def exportSheet(link):
    if link.lower() == "default":
        webbrowser.open("")
    elif link.lower() == "test":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1QliSLTkS2qLmRr64Gs0RKU-fxZ_zyoJSf3fb1uxA7nA/export?format=xlsx")

def collectMain():
    from main import anchor1V, anchor2V
    anchor1 = str(anchor1V)
    anchor2 = str(anchor2V)
    print(anchor1 + anchor2)