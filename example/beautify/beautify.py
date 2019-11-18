# coding: utf-8
import base64
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, BEAUTIFY_PATH
from example.common import get_input_file_path

output_file = os.path.dirname(os.path.abspath(__file__)) + '/output.png'

# NOTE: 以下两个参数可自行设置，取值范围[0, 100]
whitening = 100     # NOTE: 0不美白, 100代表最高程度
smoothing = 100     # NOTE: 0不磨皮, 100代表最高程度


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'whitening': whitening,
        'smoothing': smoothing
    }
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在beautify目录下')
        return
    files = {
        'image_file': open(input_file, 'rb').read()
    }
    resp = requests.post(BEAUTIFY_PATH, data=data, files=files).json()
    base64_file = resp.get('result')
    if base64_file:
        with open(output_file, 'wb') as f:
            f.write(base64.b64decode(base64_file))
    resp.pop('result', None)
    print(resp)


if __name__ == "__main__":
    call_api()
