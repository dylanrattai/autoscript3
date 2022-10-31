from index import *

anchor1 = None
anchor2 = None

def collectMain():
    from main import anchor1V, anchor2V
    anchor1 = str(anchor1V)
    anchor2 = str(anchor2V)

    print(anchor1 + anchor2)