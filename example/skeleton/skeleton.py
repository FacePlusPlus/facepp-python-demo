# coding: utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import requests

from config import API_KEY, API_SECRET, SKELETON_PATH
from example.common import get_input_file_path


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET
    }
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在skeleton目录下')
        return
    files = {
        'image_file': open(input_file, 'rb').read()
    }
    resp = requests.post(SKELETON_PATH, data=data, files=files).json()
    print(resp)


if __name__ == '__main__':
    call_api()
