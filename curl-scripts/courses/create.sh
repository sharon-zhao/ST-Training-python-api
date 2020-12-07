#!/bin/bash

curl "http://localhost:8000/course_display" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
#  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "course_display": {
      "title": "'"${TITLE}"'",
      "image_url": "'"${IMAGEURL}"'",
      "description": "'"${DESCRIPTION}"'",
      "link": "'"${LINK}"'"
    }
  }'
