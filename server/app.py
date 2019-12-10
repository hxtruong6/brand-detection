import os
from flask import Flask, flash, request, send_file, jsonify
from werkzeug.utils import secure_filename
import sys
import subprocess
from subprocess import PIPE
import re

UPLOAD_FOLDER = './uploadFiles/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ALLOWED_VIDEO_EXTENSIONS = set(['mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

result = None


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_video_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS


def process_out_info(s):
    # print("Origin result: \n" + s + "\n")
    # Predicted in 27.107808 seconds.\nCommonBuckeye: 100%\n
    lines = s.split('\n')
    # print("xxx 001 lines: " + str(lines))
    second = re.findall("\d+\.\d+", lines[0])[0]
    info = lines[1].split(': ')
    res = {
        "second": second,
        "name": info[0],
        "confidence": info[1]
    }
    print("Processed: ", str(res))
    return res


def detect(imagePath):
    darknet = b'./darknet'
    data_file = b'configFile/butterfly-obj.data'
    config_file = b'configFile/butterfly-yolov3.cfg'
    weight_file = b'butterfly-yolov3_6000.weights'
    print("Start detecting...")
    info = subprocess.run([darknet, "detector", "test", data_file, config_file, weight_file, imagePath],
                          stdout=PIPE, stderr=PIPE)
    # print(str(info)
    result = process_out_info(info.stdout.decode("utf-8"))
    print("Finish detection")
    return result


@app.route('/image', methods=['GET', 'POST'])
def image_detection():
    global result
    video_path = None
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "No image"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "No image"
        result = "Can not detect"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(video_path)
            result = detect(video_path)

    image_result = "predictions.jpg"
    return send_file(image_result, mimetype='image/*')


@app.route('/video', methods=['GET', 'POST'])
def video_detection():
    global result
    video_path = ""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "No video"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "No video"
        result = "Can not detect"
        if file and allowed_video_file(file.filename):
            filename = secure_filename(file.filename)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(video_path)
            # result = detect(video_path)

    # image_result = "predictions.jpg"
    # return send_file(image_result, mimetype='video/*')
    return result


@app.route('/result', methods=['GET'])
def image_result():
    global result
    print("Get Result: " + str(result))
    return jsonify(result)


if __name__ == '__main__':
    app.run()
