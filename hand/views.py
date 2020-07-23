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

def playersInfo(request, pk):
   hand = Hands.objects.get(id=pk)
   PlayersFormSet = inlineformset_factory(Hands, Players, fields = '__all__', extra = hand.num_of_players, max_num=hand.num_of_players)
   players = Players.objects.filter(hand=hand)
   # form = PlayerForm(initial={'hand': hand})
   formset = PlayersFormSet(instance=hand)
   if request.method == 'POST':
      try:
         formset = PlayersFormSet(request.POST, instance = hand)
         if formset.is_valid():
            # print("form is valid")
            new_player = formset.save()
            return redirect('/')
         # else:
         #    print("Form is not valid")
         #    return redirect('index')
      except Exception as e:
         print(str(e))
   context = {'hand': hand,
   'players': players,
   'formset': formset
   }
   return render(request,
   template_name = 'hand/hand_action.html',
   context = context)
