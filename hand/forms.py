from django import forms
from .models import Hands, Players


class HandForm(forms.ModelForm):
   class Meta:
      model = Hands
      fields = '__all__'

class PlayerForm(forms.ModelForm):
   class Meta:
      model =  Players
      fields = '__all__'



