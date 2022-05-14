import os

#os.system("date")
#os.mkdir("D:/Sanju/WhiteHatJr/Python Classes/class99/Folder1")
#os.getcwd()
'''
path="D:/Sanju/WhiteHatJr/Python Classes/class99/Folder1"
isExist=os.path.exists(path)
print(isExist)
'''

'''
path="D:/Sanju/WhiteHatJr/Python Classes/class99/class99.py"
root_ext=os.path.splitext(path)
print("Root part: ",root_ext[0],"\nExtension part: ",root_ext[1])
'''

#print(os.listdir("D:/Sanju/WhiteHatJr/Python Classes"))

import shutil

'''
#To copy a file
path="D:/Sanju/WhiteHatJr/Python Classes/class99"
print("Before copying: ",os.listdir(path))
source="D:/Sanju/WhiteHatJr/Python Classes/class99/Folder1/test.txt"
destination="D:/Sanju/WhiteHatJr/Python Classes/class99/testCopy.txt"
dest=shutil.copy(source,destination)
print("After copying: ",os.listdir(path))
'''

'''
#To Move a folder
path="D:/Sanju/WhiteHatJr/Python Classes/class99"
print("Before copying: ",os.listdir(path))
source="D:/Sanju/WhiteHatJr/Python Classes/class99/Folder1"
destination="D:/Sanju/WhiteHatJr/Python Classes/class99/Folder2"
dest=shutil.move(source,destination)
print("After copying: ",os.listdir(path))
'''





