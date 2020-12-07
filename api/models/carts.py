from django.db import models

from .user import User

class Cart(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    image_url = models.CharField(max_length=5000)
    title = models.CharField(max_length=5000)
    price = models.IntegerField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
