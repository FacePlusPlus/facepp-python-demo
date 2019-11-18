# coding: utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, DETECT_PATH
from example.common import get_input_file_path

return_landmark = 0
return_attributes = None
calculate_all = 0
face_rectangle = ''
beauty_score_min = 0
beauty_score_max = 100


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'return_gesture': return_landmark,
        'return_attributes': return_attributes,
        'calculate_all': calculate_all,
        'beauty_score_min': beauty_score_min,
        'beauty_score_max': beauty_score_max
    }
    if face_rectangle:
        data.update({'face_rectangle': face_rectangle})
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在detect目录下')
        return
    files = {
        'image_file': open(input_file, 'rb').read()
    }
    resp = requests.post(DETECT_PATH, data=data, files=files).json()
    print(resp)


if __name__ == "__main__":
    call_api()
