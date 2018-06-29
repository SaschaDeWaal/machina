# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.join(os.getcwd(), 'python/'))

import darknet as dn
import pdb

import cv2

from io import BytesIO
import time
import requests
from PIL import Image
import numpy as np

while (True):
    pred = []
    req = requests.get('http://10.3.141.78:5000/image.jpg') # Get frame for Blue Robot 
    curr_img = Image.open(BytesIO(req.content))
    curr_img.save("RobotB", "JPEG")

    req = requests.get('http://10.3.141.113:5000/image.jpg') # Get frame for Purple Robot
    curr_img = Image.open(BytesIO(req.content))
    curr_img.save("RobotP", "JPEG")

    req = requests.get('http://10.3.141.87:5000/image.jpg') # Get frame for Yellow Robot
    curr_img = Image.open(BytesIO(req.content))
    curr_img.save("RobotY", "JPEG")

    # Detection for Blue Robot
    dn.set_gpu(0)
    net = dn.load_net("cfg/yolo-tiny-obj.cfg", "yolo-tiny-obj_260000.weights", 0)
    meta = dn.load_meta("data/obj.data")
    r = dn.detect(net, meta, "RobotB")
    print r
    if len(r) == 0:
        continue
    else:
        for i in range(len(r)):
            pred.append(r[i][0])
            requests.post("http://10.3.141.78:5000/postdata", json={'type': pred})
        pred = []

    # Detection for Purple Robot
    r = dn.detect(net, meta, "RobotP")
    print r
    if len(r) == 0:
        continue
    else:
        for i in range(len(r)):
            pred.append(r[i][0])
            requests.post("http://10.3.141.113:5000/postdata", json={'type': pred})
        pred = []


    # Detection for Yellow Robot
    r = dn.detect(net, meta, "RobotY")
    print r
    if len(r) == 0:
        continue
    else:
        for i in range(len(r)):
            pred.append(r[i][0])
            requests.post("http://10.3.141.87:5000/postdata", json={'type': pred})
        pred = []

    time.sleep(2)



