from time import perf_counter
from threading import Thread
from level1.localdrives import getdrive
from level1.searchforfile import find
s = perf_counter()
drivee = input("enter drive ")
a = input(" searching for ")
t1 = Thread(target=getdrive)
t2 = Thread(target=find(drivee,a))
t1.start()
t2.start()
t1.join()
t2.join()
e = perf_counter()
print(f'{e-s} time taken')