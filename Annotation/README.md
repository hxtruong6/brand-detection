# Annotation
### Step 1
- Create folder Images, Labels
- List your classes in classes.txt
- In the Images and Labels folder, create subfolders corresponding to your classes
- Download images and put it in the right places
### Step 2
- Copy the pngToJpg.py and reNameFile.py from utils folder to Images folder
- Run
```
cd Images
python pngToJpg.py & python reNameFile.py
```
### Step 3
- Run and follow the tool
```
python main.py
```
### Step 4
- Create an output folder and copy all the *.jpg and *.txt in Images and Labels folder
- Move the process and the output in the same directory then run the file process.py to split the data to train and test
```
python process.py
```
### Final
output folder, train.txt and test.txt are all we need for training.
