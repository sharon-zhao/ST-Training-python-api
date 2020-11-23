from django.db import models

from .user import User

# Create your models here.
class CourseDisplay(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  url = models.UrlField(max_length=5000)
  discreption = models.CharField(max_length=5000)
  phone = models.CharField(max_length=100)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"My name is '{self.name}' this is my story {self.story}. My email is {self.email} and phone number is {self.phone}."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'name': self.name,
        'story': self.story,
        'email': self.email,
        'phone': self.phone
    }
