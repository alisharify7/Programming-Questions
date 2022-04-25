import os





















































# creator  function make dir by himself
def creator(num,name):
    for i in range(num):
        temp = str(i)
        temp1 = temp + name 
        os.mkdir(temp1)
        print("Folder %s is created" % temp1)
        print("0 Byte in folder")

num = int(input("Number of Folders :"))        
name = input("unique Name :")           

creator(num,name)