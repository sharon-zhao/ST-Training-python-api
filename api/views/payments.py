from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from decimal import *
import os

from dotenv import load_dotenv, find_dotenv
import stripe

load_dotenv(find_dotenv())

stripe.api_key = 'sk_test_51GwtbWItoru9tJqqJpxnov9vsiSPKVxI5TtnH3bG3tetqRgX7MhQBYPzJd9LKgayKpTnT1lUcDK5bOEdQ1VUYRyb00hSEAuBlK'
