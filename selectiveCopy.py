#! Walks through folder tree and copies files with a certain file ext
import os, shutil

def findAndCopyFiles(folder, fileType, newDirName='newDirCopies'):
    # Make sure folder is absolute
    parentDir = os.path.abspath(folder)
    number = 1
    while True:
        newDir = newDirName + str(number)
        path = os.path.join(parentDir, newDir)
        if not os.path.exists(path):
            break
        else:
            number = int(number) + 1
    os.mkdir(path)
    for foldername, subfolder, filenames in os.walk(folder):
        print(f'Adding folders from {foldername}')
        
        for filename in filenames:
            if filename.endswith(fileType):
                shutil.copy(filename, newDir)
                
findAndCopyFiles('folderLocation',
                 'py', 'folderForCopies')