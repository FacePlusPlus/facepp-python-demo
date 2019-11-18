# coding: utf-8
import base64
import sys
import os
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, SEGMENT_PATH
import os

return_grayscale = 0
input_dirname = os.path.abspath(os.path.dirname(__file__)) + '/input/'
output_dirname = os.path.abspath(os.path.dirname(__file__)) + '/output/'


def batch_segment():
    image_filenames = [input_dirname + filename for filename in os.listdir(input_dirname)
                       if any([filename.endswith('.png'), filename.endswith('.jpg')])]
    try:
        os.makedirs(output_dirname)
    except OSError:
        pass
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'return_grayscale': return_grayscale
    }
    for image_file in image_filenames:
        files = {
            'image_file': open(image_file, 'rb').read()
        }
        resp = requests.post(SEGMENT_PATH, data=data, files=files).json()
        body_image_file = resp.get('body_image')
        if body_image_file:
            with open(output_dirname + os.path.splitext(image_file.split('/')[-1])[0] + '.png', 'wb') as f:
                f.write(base64.b64decode(body_image_file))
        resp.pop('body_image', None)
        print(resp)


if __name__ == "__main__":
    batch_segment()
