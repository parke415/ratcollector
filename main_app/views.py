from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rat
from .forms import OutingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def rats_index(request):
  rats = Rat.objects.all()
  return render(request, 'rats/index.html', {'rats': rats})

def rats_detail(request, rat_id):
  rat = Rat.objects.get(id=rat_id)
  outing_form = OutingForm()
  return render(request, 'rats/detail.html', {
    'rat': rat,
    'outing_form': outing_form
  })

class RatCreate(CreateView):
  model = Rat
  fields = '__all__'

class RatUpdate(UpdateView):
  model = Rat
  fields = ['color', 'sex', 'age']

class RatDelete(DeleteView):
  model = Rat
  success_url = '/rats/'

def add_outing(request, rat_id):
  form = OutingForm(request.POST)
  if form.is_valid():
    new_outing = form.save(commit=False)
    new_outing.rat_id = rat_id
    new_outing.save()
  return redirect('detail', rat_id=rat_id)