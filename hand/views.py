from django.shortcuts import render, redirect
from .models import Hands, Players
from .forms import HandForm, PlayerForm

# Create your views here.
def index(request):
   hand_info = Hands.objects.all()
   player_info =  Players.objects.all()
   hand_form = HandForm()
   player_form = PlayerForm()
   context = {'hand_info': hand_info,
   'player_info': player_info,
   'hand_form': hand_form,
   'player_form': player_form
   }
   return render(request,
   template_name = 'hand/index.html',
   context = context)

def addHandInfo(request):
   if request.method == 'POST':
      # print("Printing Post", request.POST)
      hand_form = HandForm(request.POST)
      if hand_form.is_valid():
         print(hand_form.cleaned_data)
         new_hand = hand_form.save()
         hand_id = new_hand.id
         print(hand_id)
         # hand_id = new_hand.id
         return redirect('index')
      else:
         print('nie prawidlowo')
      return redirect('index')
   # context = {'hand_id': hand_id}
   # return render(request,
   # template_name = 'hands/index.html',
   # context = context)



def addPlayerInfo(request):
   if request.method == 'POST':
      try:
         player_form = PlayerForm(request.POST)
         print(request.POST)
         if player_form.is_valid():
            new_player = player_form.save()
            return redirect('index')
      except Exception as e:
         print(str(e))