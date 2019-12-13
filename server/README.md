# Server
Download file weight and put it in this directory: https://drive.google.com/open?id=1ctJCv7yHS-MxhtDTRJ3twJv5zA-ymQtk
### Go to this repo
```
cd server
```
### Create frames and output directory
```
mkdir frames
mkdir output
```
### Set up environtment
Install virtualenv
```
sudo pip2 install virtualenv
```
Create and active environment
```
virtualenv yolo
source yolo/bin/activate
```
Install opencv
```
pip install opencv-python
```

### Running detection
```
python darknet.py --input_type image --input_dir $(input directory)
```
for example:
```
python darknet.py --input_type image --input_dir test_img/test_coca.jpg
```
- The result at output/image_prediction.jpg
### Running video estimator
```
python darknet.py --input_type video --input_dir $(input directory)
```
for example:
```
python darknet.py --input_type video --input_dir uploadFiles/cocacola.mp4
```
- The video result at output/video_result.mp4
- The frequency information at output/freq.json
