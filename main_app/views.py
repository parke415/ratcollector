from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Rat, Outfit
from .forms import OutingForm

class RatCreate(CreateView):
  model = Rat
  fields = ['name', 'color', 'sex', 'age']

class RatUpdate(UpdateView):
  model = Rat
  fields = ['color', 'sex', 'age']

class RatDelete(DeleteView):
  model = Rat
  success_url = '/rats/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def rats_index(request):
  rats = Rat.objects.all()
  return render(request, 'rats/index.html', {'rats': rats})

def rats_detail(request, rat_id):
  rat = Rat.objects.get(id=rat_id)
  outfits_rat_doesnt_have = Outfit.objects.exclude(id__in=rat.outfits.all().values_list('id'))
  outing_form = OutingForm()
  return render(request, 'rats/detail.html', {
    'rat': rat,
    'outing_form': outing_form,
    'outfits': outfits_rat_doesnt_have
  })

def add_outing(request, rat_id):
  form = OutingForm(request.POST)
  if form.is_valid():
    new_outing = form.save(commit=False)
    new_outing.rat_id = rat_id
    new_outing.save()
  return redirect('detail', rat_id=rat_id)

def assoc_outfit(request, rat_id, outfit_id):
  Rat.objects.get(id=rat_id).outfits.add(outfit_id)
  return redirect('detail', rat_id=rat_id)

class OutfitList(ListView):
  model = Outfit

class OutfitDetail(DetailView):
  model = Outfit

class OutfitCreate(CreateView):
  model = Outfit
  fields = '__all__'

class OutfitUpdate(UpdateView):
  model = Outfit
  fields = ['name', 'color', 'size']

class OutfitDelete(DeleteView):
  model = Outfit
  success_url = '/outfits/'