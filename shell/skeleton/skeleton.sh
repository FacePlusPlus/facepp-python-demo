#!/usr/bin/env bash

source ../config.sh

curl -X POST "https://api-cn.faceplusplus.com/humanbodypp/v1/skeleton" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "image_file=@input.png"
