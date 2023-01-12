import os
d="C://level1"
di={}
for root,dir,files in os.walk(d):
    for d in dir:
        di[d]=os.listdir(root+"/"+d)
print(di)