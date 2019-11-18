# coding: utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, FACESET_CREATE_PATH

display_name = 'hello'
outer_id = 'fpp-demo'
tags = 'group1'
face_tokens = 'e877e8176667e12d11a5eae94937b4fa,0252a884dc2a8fd0c15360a3b0c9aee5,ebd3f7f95d6a25b722dd816d28679856'
user_data = ''
force_merge = 0


def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'display_name': display_name,
        'outer_id': outer_id,
        'tags': tags,
        'face_tokens': face_tokens,
        'user_data': user_data,
        'force_merge': force_merge
    }
    resp = requests.post(FACESET_CREATE_PATH, data=data).json()
    print(resp)


if __name__ == "__main__":
    call_api()
