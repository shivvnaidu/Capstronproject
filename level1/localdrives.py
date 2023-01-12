import win32api
import os
def getdrive():
     drives = win32api.GetLogicalDriveStrings()
     print(drives)
     drives=drives.split('\000')
     return drives
print(getdrive())
