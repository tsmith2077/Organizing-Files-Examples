#! Searches folder and removes leading zeros in filenames.
import os, re, shutil

def removeLeadingZeros(path):
    extraZerosRegex = re.compile(r"""
        ^(.*?)
        (0+)
        (\d+)
        (\.)                         
        (.*?)$
        """, re.VERBOSE)
    
    path =  os.path.abspath(path)
    for path, foldername, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(path, filename)
            mo = extraZerosRegex.search(filename)
            
            if mo == None:
                continue
            beforeNum = mo.group(1)
            numAfterZeros = mo.group(3)
            dot = mo.group(4)
            docExt = mo.group(5) 
            newFileName = beforeNum + numAfterZeros + dot + docExt
            newFilePath = os.path.join(path, newFileName)
            
            # shutil.move(filePath, newFilePath)   # uncomment to use
            
            
            print(filePath)
            print(newFilePath)  
        
        
removeLeadingZeros(
    'folderLocation'
    )