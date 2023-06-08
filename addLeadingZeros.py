#! Searches folder and adds leading zeros to files ending with numbers.
import os, re, shutil

def addLeadingZeros(path, digitLength):
    fileEndsWithNumRegex = re.compile(r"""
        ^(.*?)
        (\d+)
        (\.)                         
        (.*?)$
        """, re.VERBOSE)
    
    path =  os.path.abspath(path)
    for path, foldername, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(path, filename)
            mo = fileEndsWithNumRegex.search(filename)
            
            if mo == None:
                continue
            beforeNum = mo.group(1)
            numAfterName = mo.group(2)
            dot = mo.group(3)
            docExt = mo.group(4) 
            if len(numAfterName) > int(digitLength):
                continue
            zerosToAdd = int(digitLength) - len(numAfterName)
            newFileName = beforeNum + (zerosToAdd * '0') + numAfterName + dot + docExt
            newFilePath = os.path.join(path, newFileName)
            
            # shutil.move(filePath, newFilePath)   # uncomment to use
            
            
            print(filePath)
            print(newFilePath)  
        
        
addLeadingZeros(
    'folderLocation',
    'zeros to add')