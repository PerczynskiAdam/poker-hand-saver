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

   def __str__(self):
      return str(self.publish_date)

class Players(models.Model):
   hand = models.ForeignKey(Hands, on_delete = models.CASCADE,  null = True)
   hero = models.BooleanField(default=False, null = True, verbose_name= "Is it hero?")
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
   ]
   card_suits = [
      ('s', 'Spade'),
      ('h', 'Heart'),
      ('d', 'Diamond'),
      ('c', 'Club'),
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
   position = models.CharField(
      max_length=50,
      choices=position_choices,
      null = True, blank = True)

   first_card = models.CharField(max_length=10,
   choices = card_choices, null = True, blank = True)

   first_card_suit = models.CharField(max_length=5,
   choices=card_suits, null = True, blank = True)

   second_card = models.CharField(max_length=10,
   choices = card_choices, null = True, blank = True)

   second_card_suit = models.CharField(max_length=5,
   choices=card_suits, null = True, blank = True)

   pre_action = models.CharField(
   max_length=50,
   choices=pre_action_choices,
   null = True,
   blank = True,
   verbose_name= "PreFlop action")

   pre_act_amount = models.CharField(max_length=20, default = '', blank = True, verbose_name= "Amount")

   flop_action = models.CharField(
   max_length=50,
   choices=post_action_choices,
   null = True,
   blank = True)

   flop_act_amount = models.CharField(max_length=20, default = '', blank = True, verbose_name="Amount")


   def __str__(self):
      return self.position + "_" + self.first_card + self.second_card
   
