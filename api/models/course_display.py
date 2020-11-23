from django.db import models

# Create your models here.
class CourseDisplay(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  imageurl = models.CharField(max_length=5000)
  discreption = models.CharField(max_length=5000)
  link = models.CharField(max_length=5000)


  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'title': self.title,
        'imageurl': self.imageurl,
        'discreption': self.discreption,
        'link': self.link
    }
