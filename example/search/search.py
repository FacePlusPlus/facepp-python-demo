# coding: utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, SEARCH_PATH
from example.common import get_input_file_path

outer_id = 'fpp-demo'
return_result_count = 2
face_rectangle = ''


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'outer_id': outer_id,
        'return_result_count': return_result_count
    }
    if face_rectangle:
        data.update({'face_rectangle': face_rectangle})
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在search目录下')
        return
    files = {
        'image_file': open(input_file, 'rb').read()
    }
    resp = requests.post(SEARCH_PATH, data=data, files=files).json()
    print(resp)


if __name__ == "__main__":
    """
    调用此接口前，请先创建faceset并添加facetoken
    """
    call_api()
