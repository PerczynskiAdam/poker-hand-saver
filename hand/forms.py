from django import forms
from .models import Hands, Players


class HandForm(forms.ModelForm):
   class Meta:
      model = Hands
      fields = ['num_of_players', 'blinds']

class PlayerForm(forms.ModelForm):
   class Meta:
      model =  Players
      fields = '__all__'


