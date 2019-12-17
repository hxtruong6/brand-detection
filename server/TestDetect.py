import subprocess
from subprocess import PIPE
import re

result = None


def video_detector(videoPath):
    print("Start detecting...")
    info = subprocess.run(["python", "darknet.py", "--input_type", "image", "--input_dir", videoPath],
                          stdout=subprocess.PIPE, stderr=PIPE)
    print(str(info.stdout))
    s = (info.stdout.decode("utf-8"))
    lines = s.split('\n')
    print("xxx 001 lines: " + str(lines))
    # second = re.findall("\d+\.\d+", lines[0])[0]
    # print(second)
    # tt = lines[1].split(': ')
    # print(tt)
    # with open('freq.json', 'r') as fi:
    #     print(fi.readlines())
    print("Finish detection")
    return result


if __name__ == "__main__":
    video_detector("/media/hxtruong/Personal/College/HK_VII/ComputerVision/FinalProject/server/test_img/test_coca.jpg")
