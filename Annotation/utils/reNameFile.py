import os
from os import listdir
from os.path import isfile, join
import sys
from termcolor import colored
import re

imgType = ['jpg', 'png', 'jpeg']
count = 0


def getFileType(val):
    partFiles = val.rsplit('.', 1)
    if len(partFiles) <= 1:
        return ""
    fileType = partFiles[1].lower()
    if fileType not in imgType:
        return ""
    return fileType


def getFileName(files, dirName, fileType):
    global count
    newName = ""
    while not newName or len([i for i in files if newName in i]) > 0:
        idx = str(count)
        count = count + 1
        while len(idx) < 4:
            idx = '0' + idx
        newName = dirName + '-' + idx
    newName += '.' + fileType
    return newName

def isValid(dir, file):
    pattern = f'^({dir})d+'
    return re.search(pattern, file)


def main():
    argv = sys.argv
    defaultDir = "./"
    if argv[1] == "-d" or argv[1] == "--directory":
        dirName = argv[2]
        defaultDir += argv[2] + "/"
    editedPattern = re.compile('^' + dirName + '-[0-9]{4}\.[a-z]+')
    files = [f for f in listdir(defaultDir) if isfile(join(defaultDir, f))]
    files.sort()

    for index, val in enumerate(files):
        fileType = getFileType(val)
        if bool(editedPattern.match(val)) or not fileType or isValid(dirName, val):
            # print(val)
            continue

        newName = getFileName(files, dirName, fileType)
        print(colored(val, 'cyan') + " -> " + colored(newName, 'green'))
        # Rename
        os.rename(defaultDir + val, defaultDir + newName)


if __name__ == '__main__':
    main()
