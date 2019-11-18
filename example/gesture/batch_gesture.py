import os
import time
import shutil
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests
from config import API_KEY, API_SECRET, GESTURE_PATH

input_dirname = os.path.abspath(os.path.dirname(__file__)) + '/input/'
return_gesture = 1


def batch_gesture():
    image_filenames = [input_dirname + filename for filename in os.listdir(input_dirname)
                       if any([filename.endswith('.png'), filename.endswith('.jpg')])]
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'return_gesture': return_gesture
    }
    for image_file in image_filenames:
        files = {
            'image_file': open(image_file, 'rb').read()
        }
        resp = requests.post(GESTURE_PATH, data=data, files=files).json()
        print(resp)
        hands = resp.get('hands', [])
        for hand in hands:
            gesture = hand.get('gesture', {})
            key_name = max(gesture, key=gesture.get)
            dest_dirname = os.path.abspath(os.path.dirname(__file__)) + '/' + key_name
            if not os.path.exists(dest_dirname):
                os.makedirs(dest_dirname)
            shutil.copy(image_file, dest_dirname)
        time.sleep(2)


if __name__ == "__main__":
    batch_gesture()
