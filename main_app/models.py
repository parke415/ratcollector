from django.db import models
from django.urls import reverse
from datetime import date

ROUNDS = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('E', 'Evening')
)

class Outfit(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  size = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('outfits_detail', kwargs={'pk': self.id})

class Rat(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  sex = models.CharField(max_length=100)
  age = models.IntegerField()
  outfits = models.ManyToManyField(Outfit)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'rat_id': self.id})

  def released_for_today(self):
    return self.outing_set.filter(date=date.today()).count() >= len(ROUNDS)

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