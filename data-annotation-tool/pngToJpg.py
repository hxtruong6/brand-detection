from PIL import Image
import sys
from os import listdir, remove
from os.path import isfile, join

imgType = ['jpg', 'png', 'jpeg']


def main():
    argv = sys.argv
    defaultDir = "./"
    if argv[1] == "-d" or argv[1] == "--directory":
        defaultDir += argv[2] + "/"

    files = [f for f in listdir(defaultDir) if isfile(join(defaultDir, f))]
    files.sort()
    for img in files:
        fileType = ""
        partFiles = img.rsplit('.', 1)
        if len(partFiles) <= 1:
            continue

        fileType = partFiles[1].lower()
        if fileType in imgType and fileType == 'png':
            im = Image.open(defaultDir + img)
            rgb_im = im.convert('RGB')
            print(defaultDir + partFiles[0] + '.jpg')
            remove(defaultDir + img)
            rgb_im.save(defaultDir + partFiles[0] + '.jpg')


if __name__ == '__main__':
    main()
