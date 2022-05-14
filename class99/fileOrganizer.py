import os
import shutil


path=input("Enter the name of the directory to be organized: ")

listOfFiles=os.listdir(path)

for file in listOfFiles:
    name,ext=os.path.splitext(file)
    print("Name,ext",name,ext)
    ext=ext[1:]
    print("Ext",ext)
    if(ext==''):
        continue
    if(os.path.exists(path+"/"+ext)):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)    