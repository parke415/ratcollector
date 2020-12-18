from django.shortcuts import render
from .models import Rat

# class Rat:
#   def __init__(self, name, color, sex, age):
#     self.name = name
#     self.color = color
#     self.sex = sex
#     self.age = age

# rats = [
#   Rat('Frankie', 'brown', 'male', 1),
#   Rat('Marlowe', 'grey', 'female', 3),
#   Rat('Wally', 'brown', 'male', 2),
#   Rat('Luna', 'white', 'female', 4),
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def rats_index(request):
  rats = Rat.objects.all()
  return render(request, 'rats/index.html', {'rats': rats})

def rats_detail(request, rat_id):
  rat = Rat.objects.get(id=rat_id)
  return render(request, 'rats/detail.html', {'rat': rat})