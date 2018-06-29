from importlib import import_module
import os
from flask import Flask, render_template, Response, request
# uncomment below to use Raspberry Pi camera instead
from camera_pi import Camera

# comment this out if you're not using USB webcam
# from camera_opencv import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world!"

def gen2(camera):
    """Returns a single image frame"""
    frame = camera.get_frame()
    yield frame

@app.route('/image.jpg')
def image():
    """Returns a single current image for the webcam"""
    return Response(gen2(Camera()), mimetype='image/jpeg')

@app.route('/postdata',methods=['GET','POST'])
def postdata():
    content = request.json
    print(content)
    with open('postdata.txt', 'w') as outfile:
        json.dump(content, outfile)
    return "Posted"
if __name__ == '__main__':
    global end
    # Enter IP for each robot this file is placed in.
    app.run(host='10.3.20.78', threaded=True)
