import os
from flask import Flask, flash, request, send_file, jsonify
from werkzeug.utils import secure_filename
import subprocess
from subprocess import PIPE
import json
import re

VIDEO_UPLOAD_FOLDER = '/video_uploads/'
IMAGE_UPLOAD_FOLDER = '/test_img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ALLOWED_VIDEO_EXTENSIONS = set(['mp4'])

app = Flask(__name__)
app.config['VIDEO_UPLOAD_FOLDER'] = VIDEO_UPLOAD_FOLDER
app.config['IMAGE_UPLOAD_FOLDER'] = IMAGE_UPLOAD_FOLDER

dir_name = os.getcwd()

result = None


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_video_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS


def process_out_info(s):
    json_res = eval(s)
    # print("Json result type: ", json_res)
    res = str(json_res)
    print("Processed: ", res)
    return res


def on_detector(file_path, type="image"):
    print("Start detecting...")
    info = subprocess.run(["python", "darknet.py", "--input_type", type, "--input_dir", file_path],
                          stdout=PIPE, stderr=PIPE)
    # print(str(info))
    # print(info.stdout)

    processed_res = None
    if type == "video":
        with open("./output/freq.json", "r") as fi:
            processed_res = json.load(fi)
    else:
        # processed_res = process_out_info(info.stdout.decode("utf-8"))
        processed_res = eval(info.stdout.decode("utf-8"))

    print("Result output: ", processed_res)
    print("Finish detection")
    return processed_res


@app.route('/image', methods=['POST'])
def image_detection():
    global result
    file_path = None
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
            file_path = dir_name + os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = on_detector(file_path, "image")

    image_result = os.path.join(dir_name, "output/image_prediction.jpg")
    print(image_result)
    return send_file(image_result, mimetype='image/*')


@app.route('/video', methods=['POST'])
def video_detection():
    global result
    file_path = ""
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
        # if file and allowed_video_file(file.filename):
        if file:
            filename = secure_filename(file.filename)
            file_path = dir_name + os.path.join(app.config['VIDEO_UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = on_detector(file_path, "video")

    video_result = os.path.join(dir_name, "output/video_result.mp4")
    return send_file(video_result, mimetype='video/*')


@app.route('/result', methods=['GET'])
def image_result():
    global result
    print("Get Result: " + str(result))
    return jsonify(result)


if __name__ == '__main__':
    app.run()
