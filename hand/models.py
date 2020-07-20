from django.db import models

# Create your models here.
class Hands(models.Model):
   blind_choices = [
      ('1/2', '1/2'),
      ('2/5', '2/5'),
   ]
   blinds = models.CharField(
      max_length=10,
      choices=blind_choices,
      default= '1/2'
   )

   num_of_players = models.IntegerField()
   publish_date = models.DateTimeField(auto_now_add=True)
   @property
   def potSize(self):
      sb = self.blinds.split('/')[0]
      bb = self.blinds.split('/')[1]
      potsize = int(sb) + int(bb)
      return potsize

   def __str__(self):
      return str(self.id)

class Players(models.Model):
   hand = models.ForeignKey(Hands, on_delete = models.SET_NULL,  null = True)
   hero = models.BooleanField(default=False, null = True)
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
   ]
   pre_action_choices = [
      ('Raise','raise'),
      ('Fold','fold'),
      ('Call','call'),
      ('Check', 'check')
   ]
   post_action_choices = [
      ('Raise','raise'),
      ('Fold','fold'),
      ('Call','call'),
      ('Check', 'check'),
      ('Check/Fold', 'checkfold'),
      ('Bet','bet'),
   ]
   position = models.CharField(
      max_length=50,
      choices=position_choices,
      null = True, blank = True)

   first_card = models.CharField(max_length=10,
   choices = card_choices, null = True, blank = True)

   second_card = models.CharField(max_length=10,
   choices = card_choices, null = True, blank = True)

   pre_action = models.CharField(
   max_length=50,
   choices=pre_action_choices,
   null = True,
   blank = True)

   flop_action = models.CharField(
   max_length=50,
   choices=post_action_choices,
   null = True,
   blank = True)

   pre_act_amount = models.CharField(max_length=50, default = '', blank = True)
   flop_act_amount = models.CharField(max_length=50, default = '', blank = True)


   def __str__(self):
      return self.position + "_" + self.first_card + self.second_card
   
