import multiprocessing as mp
from level1 . searchforfile import find
from level1 . localdrives import getdrive
from time import perf_counter
def drive():
    getdrive()
def searchfile(name,path):
    find(name,path)
if __name__=='__main__':
    start_time=perf_counter()
    print("Number of processors:",mp.cpu_count())
    name=input("enter the file name:")
    path=input("enter the path")
    p1=mp.Process(target=drive)
    p2=mp.Process(target=searchfile,args=(name,path))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time=perf_counter()
    print(f'{end_time-start_time} seconds taken')
