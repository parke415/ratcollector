from django.shortcuts import render
from django.http import HttpResponse

class Rat:
  def __init__(self, name, color, sex, age):
    self.name = name
    self.color = color
    self.sex = sex
    self.age = age

rats = [
  Rat('Frankie', 'brown', 'male', 1),
  Rat('Marlowe', 'grey', 'female', 3),
  Rat('Wally', 'brown', 'male', 2),
  Rat('Luna', 'white', 'female', 4),
]

def home(request):
  return HttpResponse('<h1>Hello ᘛ⁐̤ᕐᐷ</h1>')

def about(request):
  return render(request, 'about.html')

def rats_index(request):
  return render(request, 'rats/index.html', { 'rats': rats })