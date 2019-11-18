#!/usr/bin/env bash

source ../config.sh

template_rectangle=''
merge_rectangle=''
merge_rate=50

curl -X POST "https://api-cn.faceplusplus.com/imagepp/v1/mergeface" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "template_file=@input1.jpg" \
-F "merge_file=@input2.jpg" \
-F "merge_rate=${merge_rate}"