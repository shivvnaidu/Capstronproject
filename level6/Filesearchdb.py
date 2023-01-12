import os
import threading
import logging
from level3.demo_exception import FileSearcher
from searchfileDB import SearchDB
from level5.demo_searchlog import Searchlog
if __name__=='__main__':
    data=[]
    drive=input("enter drive")
    file_name=input("enter file name")
    obj=FileSearcher()
    dbobj=SearchDB()
    dbobj1=Searchlog()
    res=dbobj.searDB(file_name)

    if res==0:
        data=obj.search(drive,file_name)
        print(data)
        try:
            print(data[0])
            dbobj.insertDB(data[0])
            logging.info(data[0])
        except IndexError:
            print("no file exists")

        else:
            print(res)
