from django.db import models

class Rat(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  sex = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.name
