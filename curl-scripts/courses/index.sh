#!/bin/bash

curl "http://localhost:8000/course_display" \
  --include \
  --request GET \
#  --header "Authorization: Token ${TOKEN}"

echo
