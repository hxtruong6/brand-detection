from PIL import Image
import sys
from os import listdir, remove
from os.path import isfile, join
from termcolor import colored


def main():
    argv = sys.argv
    if argv[1] == "-d" or argv[1] == "--directory":
        directory = argv[2]
    imageDir = './Images/' + directory + "/"
    labelDir = './Labels/' + directory + "/"

    images = [f for f in listdir(imageDir) if isfile(join(imageDir, f))]
    labels = [f for f in listdir(labelDir) if isfile(join(labelDir, f))]

    images.sort()
    labels.sort()
    count = 0
    for img in images:
        fileType = ""
        partFiles = img.rsplit('.', 1)
        if len(partFiles) <= 1:
            continue

        if partFiles[0] + '.txt' not in labels:
            print(colored("Delete image: ", 'red') + img)
            count = count + 1
            remove(imageDir + img)
	

    for label in labels:
        if "(1)" in label:
            print(colored("Delete label: ", 'red') + label)
            count = count + 1
            remove(labelDir + label)
    print('Delete total ' + str(count) + ' files')


if __name__ == '__main__':
    main()
