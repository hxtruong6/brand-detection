import glob, os
os.chdir("./output")
cnt_jpg = 0
cnt_txt = 0
for file in glob.glob("*.txt"):
    cnt_txt += 1

for file in glob.glob("*.jpg"):
    cnt_jpg += 1


print(cnt_jpg, cnt_txt, len(os.listdir('.')))
assert cnt_jpg==cnt_txt
