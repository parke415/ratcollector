from django.forms import ModelForm
from .models import Outing

class OutingForm(ModelForm):
  class Meta:
    model = Outing
    fields = ['date', 'round']
    