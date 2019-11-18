# coding: utf-8
import os


def get_input_file_path(dirname, file_name):
    exts = ['.png', '.jpg']
    for ext in exts:
        if os.path.exists(dirname + '/' + file_name + ext):
            return dirname + '/' + file_name + ext

