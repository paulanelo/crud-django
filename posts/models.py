from django.db import models

# Create your models here.

class Post(models.Model):
  legend = models.TextField()
  photo = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.legend
