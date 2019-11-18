#!/usr/bin/env bash

source ../config.sh

whitening=100
smoothing=100

curl -X POST "https://api-cn.faceplusplus.com/facepp/v1/beautify" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "whitening=${whitening}" \
-F "smoothing=${smoothing}" \
-F "image_file=@input.png"