from django.db import models

# Create your models here.
class Hands(models.Model):
   blind_choices = [
      ('1/2', '1/2'),
      ('2/5', '2/5'),
   ]
   player_choices = [
      (2, '2'),
      (3, '3')
   ]
   blinds = models.CharField(
      max_length=10,
      choices=blind_choices,
      default= '1/2'
   )

   num_of_players = models.IntegerField(
      choices=player_choices,
      verbose_name= "Nr of players",
      default=2)
   publish_date = models.DateTimeField(auto_now_add=True)

   @property
   def potSize(self):
      sb = self.blinds.split('/')[0]
      bb = self.blinds.split('/')[1]
      potsize = int(sb) + int(bb)
      return potsize
      
   @property
   def flopPotSize(self):
      players = self.players_set.all()
      pre = sum([sum([int(k) for k in j]) if isinstance(j, list) else int(j) for j in [i.pre_act_amount.split('/') if '/' in i.pre_act_amount else i.pre_act_amount for i in players]])
      potsize = pre + self.potSize
      return potsize 

   @property
   def turnPotSize(self):
      players = self.players_set.all()
      flop = sum([sum([int(k) for k in j]) if isinstance(j, list) else int(j) for j in [i.flop_act_amount.split('/') if '/' in i.flop_act_amount else i.flop_act_amount for i in players]])
      potsize =  flop + self.flopPotSize
      return potsize 

   @property
   def riverPotSize(self):
      players = self.players_set.all()
      turn = sum([sum([int(k) for k in j]) if isinstance(j, list) else int(j) for j in [i.turn_act_amount.split('/') if '/' in i.turn_act_amount else i.turn_act_amount for i in players]])
      potsize =  turn + self.turnPotSize
      return potsize 

   def __str__(self):
      return str(self.publish_date)

class Players(models.Model):
   hand = models.ForeignKey(Hands, on_delete = models.CASCADE,  null = True)
   hero_choices = [
      ('H', 'Hero'),
      (' ', 'Villain')
   ]
   position_choices = [
      ('UTG', 'Under The Gun'),
      ('MP', 'Middle Position'),
      ('CO', 'Cut-off'),
      ('BTN', 'Button'),
      ('SB', 'Small Blind'),
      ('BB', 'Big Blind'),
   ]
   card_choices = [
      ('A', 'A'),
      ('K', 'K'),
      ('Q', 'Q'),
      ('J', 'J'),
      ('T', 'T'),
      ('9', '9'),
      ('8', '8'),
      ('7', '7'),
      ('6', '6'),
      ('5', '5'),
      ('4', '4'),
      ('3', '3'),
      ('2', '2'),
      (' ', 'Unk'),
   ]
   card_suits = [
      ('s', 'Spade'),
      ('h', 'Heart'),
      ('d', 'Diamond'),
      ('c', 'Club'),
      (' ', 'Unk'),
   ]
   pre_action_choices = [
      ('F','Fold'),
      ('X', 'Check'),
      ('L', 'Limp'),
      ('C','Call'),
      ('R','Raise'),
      ('L/F', 'Limp/Fold'),
      ('L/C', 'Limp/Call'),
      ('L/R', 'Limp/Raise'),
      ('C/F', 'Call/Fold'),
      ('C/C', 'Call/Call'),
      ('C/R', 'Call/Raise'),
      ('R/F', 'Raise/Fold'),
      ('R/C', 'Raise/Call'),
      ('R/R', 'Raise/Raise'),
   ]
   post_action_choices = [
      ('F','Fold'),
      ('X', 'Check'),
      ('L', 'Limp'),
      ('C', 'Call'),
      ('B', 'Bet'),
      ('R', 'Raise'),
      ('X/F', 'Check/Fold'),
      ('X/C', 'Check/Call'),
      ('X/R', 'Check/Raise'),
      ('L/F', 'Limp/Fold'),
      ('L/C', 'Limp/Call'),
      ('L/R', 'Limp/Raise'),
      ('C/F', 'Call/Fold'),
      ('C/C', 'Call/Call'),
      ('C/R', 'Call/Raise'),
      ('B/F', 'Bet/Fold'),
      ('B/C', 'Bet/Call'),
      ('B/R', 'Bet/Raise'),
      ('R/F', 'Raise/Fold'),
      ('R/C', 'Raise/Call'),
      ('R/R', 'Raise/Raise'),
   ]

   hero = models.CharField(max_length=10, choices=hero_choices, default='', verbose_name= "Is it hero?")
   
   position = models.CharField(
      max_length=50,
      choices=position_choices,
      null = True, blank = True)

   stack = models.PositiveSmallIntegerField(default = 200)

   first_card = models.CharField(max_length=2,
   choices = card_choices, null = True, blank = True, default= ' ')

   first_card_suit = models.CharField(max_length=10,
   choices=card_suits, null = True, blank = True, default= ' ')

   second_card = models.CharField(max_length=2,
   choices = card_choices, null = True, blank = True, default= ' ')

   second_card_suit = models.CharField(max_length=10,
   choices=card_suits, null = True, blank = True, default= ' ')

   pre_action = models.CharField(
   max_length=50,
   choices=pre_action_choices,
   null = True,
   blank = True,
   verbose_name= "PreFlop action")

   pre_act_amount = models.CharField(max_length=20, default = '0', blank = True, verbose_name= "Amount")

   flop_action = models.CharField(
   max_length=50,
   choices=post_action_choices,
   null = True,
   blank = True)

   flop_act_amount = models.CharField(max_length=20, default = '0', blank = True, verbose_name="Amount")

   turn_action = models.CharField(
   max_length=50,
   choices=post_action_choices,
   null = True,
   blank = True)

   turn_act_amount =  models.CharField(max_length=20, default = '0', blank = True, verbose_name="Amount")
   
   river_action = models.CharField(
   max_length=50,
   choices=post_action_choices,
   null = True,
   blank = True)

   river_act_amount =  models.CharField(max_length=20, default = '0', blank = True, verbose_name="Amount")



   @property
   def handCards(self):
      hand_cards = self.first_card + self.first_card_suit + ' ' + self.second_card + self.second_card_suit
      return hand_cards


   def __str__(self):
      return self.position + "_" + self.first_card + self.second_card
   
