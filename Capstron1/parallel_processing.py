import multiprocessing as mp
from level1 . searchforfile import find
from level1 . localdrives import getdrive
from time import perf_counter
from threading import Thread
def drives():
    getdrive()
def search():
    find(name,path)
start_time=perf_counter()
name=input("enter the name of the file:")
path=input("enter the path:")
t1=Thread(target=drives)
t2=Thread(target=search)
t1.start()
t2.start()
t1.join()
t2.join()
print("Number of processors:",mp.cpu_count())
end_time=perf_counter()
print(f"{end_time-start_time} seconds taken")

