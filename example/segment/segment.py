# coding: utf-8
import base64
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, SEGMENT_PATH
from example.common import get_input_file_path

return_grayscale = 1


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'return_grayscale': return_grayscale
    }
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在segment目录下')
        return
    files = {
        'image_file': open(input_file, 'rb').read()
    }
    resp = requests.post(SEGMENT_PATH, data=data, files=files).json()
    result_file = resp.get('result')
    body_image_file = resp.get('body_image')
    if result_file:
        with open(os.path.abspath(os.path.dirname(__file__)) + '/mask.png', 'wb') as f:
            f.write(base64.b64decode(result_file))
    resp.pop('result', None)

    if body_image_file:
        with open(os.path.abspath(os.path.dirname(__file__)) + '/output.png', 'wb') as f:
            f.write(base64.b64decode(body_image_file))
    resp.pop('body_image', None)
    print(resp)


if __name__ == '__main__':
    call_api()
