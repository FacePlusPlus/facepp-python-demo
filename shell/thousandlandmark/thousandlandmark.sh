#!/usr/bin/env bash

source ../config.sh

return_landmark='all'

curl -X POST "https://api-cn.faceplusplus.com/facepp/v1/face/thousandlandmark" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "image_file=@input.png" \
-F "return_landmark=${return_landmark}"
