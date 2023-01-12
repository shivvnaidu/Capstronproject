from . import localdrives as dd
import os
def find(name,path):
    for i in path:
        for root,dir,files in os.walk(i):
            for j in files:
                if j==name:
                    print(" file is present ")
                    print(root)
                    break
name = input(" enter the filename \n ")
path=dd.getdrive()
find(name,path)