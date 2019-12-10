import os
from os import listdir
from os.path import isfile, join
import sys
from termcolor import colored
import re

imgType = ['jpg']
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

    cnt_txt = 0
    cnt_jpg = 0
    for index, val in enumerate(files):
        fileType = getFileType(val)
        
        if bool(editedPattern.match(val)) or not fileType or isValid(dirName, val):
            # print(val)
            #os.remove(defaultDir+val)
            continue


        name_wt_ext, ext = os.path.splitext(val)[0], os.path.splitext(val)[1]

        if ext[1:] == 'jpg' :
            cnt_jpg+=1
        else:
            #os.remove(defaultDir+val)
            continue
        

        #print(name_wt_ext)
        annotation_name = name_wt_ext + '.txt'
        #print(annotation_name)
        
        if isfile(join(defaultDir, annotation_name)):
            cnt_txt += 1
            newName = getFileName(files, dirName, fileType)
            new_annotation_name = os.path.splitext(newName)[0] + '.txt'
            #print(new_annotation_name)
            #print(newName)
            print(colored(val, 'cyan') + " -> " + colored(newName, 'green'))
            print(colored(annotation_name, 'cyan') + " -> " + colored(new_annotation_name, 'green'))
            # Rename
            os.rename(defaultDir + val, defaultDir + newName)
            os.rename(defaultDir + annotation_name, defaultDir + new_annotation_name)

    print(cnt_jpg, cnt_txt)
    #assert cnt_jpg == cnt_txt

if __name__ == '__main__':
    main()
