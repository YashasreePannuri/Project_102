import os
import shutil

fromdirectory="C:/Users/sreel/Downloads/"
todirectory="C:/Users/sreel/Downloads/files"
listoffiles=os.listdir(fromdirectory)
print(listoffiles)

for filename in listoffiles:
    name,extention=os.path.splitext(filename)

    if extention == " ":
        continue
    if extention in ['.txt','.doc','.docx','.pdf']:
        path1 = fromdirectory + '/' + filename
        path2 = todirectory + '/' + "Document_Files"
        path3 = todirectory + '/' + "Documemt_Files" + '/' + filename
        if os.path.exists(path2):
            print("Moving " + filename + ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + filename + ".....")
            shutil.move(path1,path3)