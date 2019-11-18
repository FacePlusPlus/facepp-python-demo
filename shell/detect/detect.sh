#!/usr/bin/env bash

source ../config.sh

return_landmark=0
return_attributes='gender,age'
calculate_all=0
beauty_score_min=0
beauty_score_max=100

curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "image_file=@input.jpg" \
-F "return_landmark=${return_landmark}" \
-F "return_attributes=${return_attributes}" \
-F "calculate_all=${calculate_all}" \
-F "beauty_score_min=${beauty_score_min}" \
-F "beauty_score_max=${beauty_score_max}"
