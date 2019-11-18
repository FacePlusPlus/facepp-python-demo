#!/usr/bin/env bash

source ../config.sh

display_name='hello'
outer_id='fpp-demo2'
tags='group2'
face_tokens='e877e8176667e12d11a5eae94937b4fa,0252a884dc2a8fd0c15360a3b0c9aee5,ebd3f7f95d6a25b722dd816d28679856'
user_data=''
force_merge=0

curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faceset/create" \
-F "api_key=${API_KEY}" \
-F "api_secret=${API_SECRET}" \
-F "display_name=${display_name}" \
-F "outer_id=${outer_id}" \
-F "tags=${tags}" \
-F "face_tokens=${face_tokens}" \
-F "user_data=${user_data}" \
-F "force_merge=${force_merge}"
