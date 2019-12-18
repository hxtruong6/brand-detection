from ctypes import *
import math
import random
import cv2
import os
import argparse
import json
import glob


def sample(probs):
    s = sum(probs)
    probs = [a / s for a in probs]
    r = random.uniform(0, 1)
    for i in range(len(probs)):
        r = r - probs[i]
        if r <= 0:
            return i
    return len(probs) - 1


def c_array(ctype, values):
    arr = (ctype * len(values))()
    arr[:] = values
    return arr


class BOX(Structure):
    _fields_ = [("x", c_float),
                ("y", c_float),
                ("w", c_float),
                ("h", c_float)]


class DETECTION(Structure):
    _fields_ = [("bbox", BOX),
                ("classes", c_int),
                ("prob", POINTER(c_float)),
                ("mask", POINTER(c_float)),
                ("objectness", c_float),
                ("sort_class", c_int)]


class IMAGE(Structure):
    _fields_ = [("w", c_int),
                ("h", c_int),
                ("c", c_int),
                ("data", POINTER(c_float))]


class METADATA(Structure):
    _fields_ = [("classes", c_int),
                ("names", POINTER(c_char_p))]


dir_name = os.getcwd()
lib_darknet_dir = os.path.join(dir_name, "libdarknet.so")
lib_darknet_dir = lib_darknet_dir.encode('utf-8')
# lib = CDLL("/home/pjreddie/documents/darknet/libdarknet.so", RTLD_GLOBAL)
lib = CDLL(lib_darknet_dir, RTLD_GLOBAL)
lib.network_width.argtypes = [c_void_p]
lib.network_width.restype = c_int
lib.network_height.argtypes = [c_void_p]
lib.network_height.restype = c_int

predict = lib.network_predict
predict.argtypes = [c_void_p, POINTER(c_float)]
predict.restype = POINTER(c_float)

set_gpu = lib.cuda_set_device
set_gpu.argtypes = [c_int]

make_image = lib.make_image
make_image.argtypes = [c_int, c_int, c_int]
make_image.restype = IMAGE

get_network_boxes = lib.get_network_boxes
get_network_boxes.argtypes = [c_void_p, c_int, c_int, c_float, c_float, POINTER(c_int), c_int, POINTER(c_int)]
get_network_boxes.restype = POINTER(DETECTION)

make_network_boxes = lib.make_network_boxes
make_network_boxes.argtypes = [c_void_p]
make_network_boxes.restype = POINTER(DETECTION)

free_detections = lib.free_detections
free_detections.argtypes = [POINTER(DETECTION), c_int]

free_ptrs = lib.free_ptrs
free_ptrs.argtypes = [POINTER(c_void_p), c_int]

network_predict = lib.network_predict
network_predict.argtypes = [c_void_p, POINTER(c_float)]

reset_rnn = lib.reset_rnn
reset_rnn.argtypes = [c_void_p]

load_net = lib.load_network
load_net.argtypes = [c_char_p, c_char_p, c_int]
load_net.restype = c_void_p

do_nms_obj = lib.do_nms_obj
do_nms_obj.argtypes = [POINTER(DETECTION), c_int, c_int, c_float]

do_nms_sort = lib.do_nms_sort
do_nms_sort.argtypes = [POINTER(DETECTION), c_int, c_int, c_float]

free_image = lib.free_image
free_image.argtypes = [IMAGE]

letterbox_image = lib.letterbox_image
letterbox_image.argtypes = [IMAGE, c_int, c_int]
letterbox_image.restype = IMAGE

load_meta = lib.get_metadata
lib.get_metadata.argtypes = [c_char_p]
lib.get_metadata.restype = METADATA

load_image = lib.load_image_color
load_image.argtypes = [c_char_p, c_int, c_int]
load_image.restype = IMAGE

rgbgr_image = lib.rgbgr_image
rgbgr_image.argtypes = [IMAGE]

predict_image = lib.network_predict_image
predict_image.argtypes = [c_void_p, IMAGE]
predict_image.restype = POINTER(c_float)


def classify(net, meta, im):
    out = predict_image(net, im)
    res = []
    for i in range(meta.classes):
        res.append((meta.names[i], out[i]))
    res = sorted(res, key=lambda x: -x[1])
    return res


def detect(net, meta, image, thresh=.1, hier_thresh=.5, nms=.45):
    image = image.encode('utf-8')
    im = load_image(image, 0, 0)
    num = c_int(0)
    pnum = pointer(num)
    predict_image(net, im)
    dets = get_network_boxes(net, im.w, im.h, thresh, hier_thresh, None, 0, pnum)
    num = pnum[0]
    if (nms): do_nms_obj(dets, num, meta.classes, nms);

    res = []
    for j in range(num):
        for i in range(meta.classes):
            if dets[j].prob[i] > 0:
                b = dets[j].bbox
                res.append((meta.names[i], dets[j].prob[i], (b.x, b.y, b.w, b.h)))
    res = sorted(res, key=lambda x: -x[1])
    free_image(im)
    free_detections(dets, num)
    return res


def get_prediction_image(net, meta, image_dir):
    r = detect(net, meta, image_dir)
    img = cv2.imread(image_dir)
    img_h, img_w = img.shape[:2]
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1.1

    cls_color = {
        'Lavie': (0, 255, 0),
        'Coca': (0, 0, 0),
        'VinhHao': (255, 0, 0),
        'Dasani': (255, 255, 0),
        'Aquafina': (0, 0, 255)
    }

    cls = set()
    confidence_cls = []
    cum_area =  {
        'Lavie': 0.0,
        'Coca': 0.0,
        'VinhHao': 0.0,
        'Dasani': 0.0,
        'Aquafina': 0.0
    }
    for det in r:
        x, y, w, h = map(int, det[2])
        x = x - int(w / 2)
        y = y - int(h / 2)
        text = str(det[0].decode('utf-8'))
        cls.add(text)
        confidence_cls.append(
            {'class': text, 'confidence': det[1]})

        cum_area[text] += w*h / (img_w * img_h)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), cls_color[text], 2)
        (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
        box_coords = ((x, y - 1), (x + text_width + 2, y - 1 - text_height - 2))
        cv2.rectangle(img, box_coords[0], box_coords[1], cls_color[text], cv2.FILLED)
        img = cv2.putText(img, text, (x - 1, y - 1), font, fontScale=font_scale, color=(255, 255, 255), thickness=1)

    return img, cls, confidence_cls, cum_area


def get_video_estimator(net, meta, video_dir):
    # video processing
    print('video dir: ', video_dir)
    vidcap = cv2.VideoCapture(video_dir)
    success, image = vidcap.read()
    count = 0

    cls_cnt_freq = {
        'Lavie': 0,
        'Coca': 0,
        'VinhHao': 0,
        'Dasani': 0,
        'Aquafina': 0
    }

    video_cum_area_ratio = {
        'Lavie': 0.0,
        'Coca': 0.0,
        'VinhHao': 0.0,
        'Dasani': 0.0,
        'Aquafina': 0.0
    }

    while success:
        cur_frame_dir = "frames/frame%d.jpg" % count
        cv2.imwrite(cur_frame_dir, image)  # save frame as JPEG file
        predict_img, cls, _, cum_area = get_prediction_image(net, meta, cur_frame_dir)

        for cls_txt in cls:
            cls_cnt_freq[cls_txt] += 1

        for key in cum_area.keys():
            video_cum_area_ratio[key] += cum_area[key]

        cv2.imwrite(cur_frame_dir, predict_img)
        success, image = vidcap.read()
        print('Read a new frame: ', success, count)
        count += 1

    for key in video_cum_area_ratio.keys():
        if cls_cnt_freq[key] > 0:
            video_cum_area_ratio[key] /= (cls_cnt_freq[key] *1.0)
        else:
            video_cum_area_ratio[key] = 0.0 

    for key in cls_cnt_freq.keys():
        cls_cnt_freq[key] /= 1.0 * count

    result_dict = {
        'freq': cls_cnt_freq,
        'cover': video_cum_area_ratio
    }

    with open('output/template_result.json', 'w') as fb:
        json.dump(result_dict, fb)


    '''
    with open('output/freq.json', 'w') as fb:
        json.dump(cls_cnt_freq, fb)
        json.dump(video_cum_area_ratio, fb)

    with open('output/area.json', 'w') as fb:
        json.dump(video_cum_area_ratio, fb)
    '''

    #print('Num frame: ', count)
    return cls_cnt_freq


def create_video_from_frames(frames_dir):
    img_array = []
    print("frame: ", frames_dir)
    print("curr dir: ", dir_name)
    for filename in sorted(glob.glob(frames_dir + '/*.jpg'), key=os.path.getmtime, reverse=False):
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('output/video_result.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    for i in range(len(img_array)):
        out.write(img_array[i])

    out.release()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_type', type=str, default='image')
    parser.add_argument('--input_dir', type=str, default='test_img/test_coca.jpg')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # net = load_net("cfg/densenet201.cfg", "/home/pjreddie/trained/densenet201.weights", 0)
    # im = load_image("data/wolf.jpg", 0, 0)
    # meta = load_meta("cfg/imagenet1k.data")
    # r = classify(net, meta, im)
    # print r[:10]

    # declare necessary directories
    weight_dir = os.path.join(dir_name, "brand-yolov3_5000.weights")
    weight_cfg_dir = os.path.join(dir_name, "cfg/brand-yolov3.cfg")
    meta_dir = os.path.join(dir_name, "cfg/brand-obj.data")
    weight_dir = weight_dir.encode('utf-8')
    weight_cfg_dir = weight_cfg_dir.encode('utf-8')
    meta_dir = meta_dir.encode('utf-8')

    # load weight and meta
    net = load_net(weight_cfg_dir, weight_dir, 0)
    meta = load_meta(meta_dir)

    args = parse_args()
    input_dir = os.path.join(dir_name, args.input_dir)
    # input_dir = input_dir.encode('utf-8')

    if args.input_type == 'image':
        pred_img, _, confidence_cls, _ = get_prediction_image(net, meta, input_dir)
        print(confidence_cls)
        cv2.imwrite("output/image_prediction.jpg", pred_img)
    elif args.input_type == 'video':
        video_estimation = get_video_estimator(net, meta, input_dir)
        print(video_estimation)
        create_video_from_frames('frames')
    else:
        print('Invalid input type, image and video only')
