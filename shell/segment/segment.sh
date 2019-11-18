#!/usr/bin/env bash

source ../config.sh

return_grayscale=1

curl -X POST "https://api-cn.faceplusplus.com/humanbodypp/v2/segment" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "image_file=@input.jpg" \
-F "return_grayscale=${return_grayscale}"
