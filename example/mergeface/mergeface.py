# coding: utf-8
import base64
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import requests

from config import API_KEY, API_SECRET, MERGEFACE_PATH
from example.common import get_input_file_path

output_file = os.path.abspath(os.path.dirname(__file__)) + '/output.png'

template_rectangle = ''
merge_rectangle = ''
merge_rate = 50


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'merge_rate': merge_rate
    }
    if template_rectangle:
        data.update({'template_rectangle': template_rectangle})
    if merge_rectangle:
        data.update({'merge_rectangle': merge_rectangle})

    template_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input1')
    merge_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input2')
    if not all([template_file, merge_file]):
        print('请将input1.png/input1.jpg, input2.png/input2.jpg文件放在mergeface目录下')
        return
    files = {
        'template_file': open(template_file, 'rb').read(),
        'merge_file': open(merge_file, 'rb').read()
    }

    resp = requests.post(MERGEFACE_PATH, data=data, files=files).json()
    base64_file = resp.get('result')
    if base64_file:
        with open(output_file, 'wb') as f:
            f.write(base64.b64decode(base64_file))
    resp.pop('result', None)
    print(resp)


if __name__ == "__main__":
    call_api()
