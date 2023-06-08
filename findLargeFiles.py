#! Walks through folder tree and finds files that are greater than 
# the number of bytes entered.
import os

def findFilesLargerThan(path, units='bytes', size=2000):
    dirToSearch = os.path.abspath(path)
    exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
    
    for path, foldername, filesnames in os.walk(dirToSearch):
        for filename in filesnames:
            filePath = os.path.join(path, filename)
            fileSize = os.path.getsize(filePath)
            if units not in exponents_map:
                raise ValueError("Must select from ['bytes', 'kb', 'mb', 'gb']")
            else:
                fileSize = fileSize / 1024 ** exponents_map[units]
                if fileSize > size:
                    print(f'Filename: {filename}')
                    print(f'Filesize: {round(fileSize, 3)} {units}')
                    print(filePath)

    
findFilesLargerThan(
    'folderLocation',
    'fileSizeUnits', 10)