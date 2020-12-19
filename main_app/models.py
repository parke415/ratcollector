from django.db import models
from django.urls import reverse

ROUNDS = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('E', 'Evening')
)

class Rat(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  sex = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'rat_id': self.id})

class Outing(models.Model):
  date = models.DateField('outing date')
  round = models.CharField(
    max_length=1,
    choices=ROUNDS,
    default=ROUNDS[0][0]
  )

  rat = models.ForeignKey(Rat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_round_display()} on {self.date}"

  class Meta:
    ordering = ['-date']