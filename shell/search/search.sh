#!/usr/bin/env bash

source ../config.sh

outer_id='fpp-demo2'
return_result_count=2

curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/search" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "outer_id=${outer_id}" \
-F "return_result_count=${return_result_count}" \
-F "image_file=@input.jpg"
