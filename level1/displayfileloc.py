import os
counter = 0
a = input("what your searching for? :>")
thisdir = os.getcwd()
for root,directory,filename in os.walk("/level1//"):
    for file in filename :
        filepath = os.path.join(root,file)
        if a in file:
            counter +=1
            print(os.path.join(root,file))
if counter == 0:
    print(" no file found ")
else:
    print(f"{counter} files.")
