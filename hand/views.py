from django.shortcuts import render, redirect
from .models import Hands, Players
from django.forms import inlineformset_factory
from .forms import HandForm, PlayerForm

# Create your views here.
def index(request):
   hands = Hands.objects.all()
   hand_form = HandForm()
   context = {'hands': hands,
   'hand_form': hand_form
   }
   return render(request,
   template_name = 'hand/index.html',
   context = context)

def addHandInfo(request):
   if request.method == 'POST':
      hand_form = HandForm(request.POST)
      if hand_form.is_valid():
         hand_form.save()

         return redirect('index')
      else:
         print('nie prawidlowo')
      return redirect('index')


def playersInfo(request, pk):
   hand = Hands.objects.get(id=pk)
   PlayersFormSet = inlineformset_factory(Hands, Players, fields = '__all__', extra = hand.num_of_players, max_num=hand.num_of_players)
   players = Players.objects.filter(hand=hand)
   formset = PlayersFormSet(instance=hand)
   hand_form = HandForm(instance=hand)
   if request.method == 'POST':
      formset = PlayersFormSet(request.POST, instance = hand)
      hand_form = HandForm(request.POST, instance = hand)
      # print(formset.errors)
      if formset.is_valid() and hand_form.is_valid():
         formset.save()
         hand_form.save()
         return redirect('/')
      else:
         print("Form is not valid")


   context = {'hand': hand,
   'players': players,
   'formset': formset,
   'hand_form': hand_form
   }
   return render(request,
   template_name = 'hand/hand_action.html',
   context = context)

def deleteHand(request, pk):
   hand = Hands.objects.get(id=pk)
   hand.delete()
   return redirect('/')
