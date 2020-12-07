from django.db import models


# Create your models here.
class CourseDisplay(models.Model):
    # define fields

    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    link = models.CharField(max_length=5000)

