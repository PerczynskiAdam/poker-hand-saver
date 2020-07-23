# Generated by Django 3.0.8 on 2020-07-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0012_auto_20200723_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='river_act_amount',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='players',
            name='river_action',
            field=models.CharField(blank=True, choices=[('F', 'Fold'), ('X', 'Check'), ('L', 'Limp'), ('C', 'Call'), ('B', 'Bet'), ('R', 'Raise'), ('X/F', 'Check/Fold'), ('X/C', 'Check/Call'), ('X/R', 'Check/Raise'), ('L/F', 'Limp/Fold'), ('L/C', 'Limp/Call'), ('L/R', 'Limp/Raise'), ('C/F', 'Call/Fold'), ('C/C', 'Call/Call'), ('C/R', 'Call/Raise'), ('B/F', 'Bet/Fold'), ('B/C', 'Bet/Call'), ('B/R', 'Bet/Raise'), ('R/F', 'Raise/Fold'), ('R/C', 'Raise/Call'), ('R/R', 'Raise/Raise')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='turn_act_amount',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='players',
            name='turn_action',
            field=models.CharField(blank=True, choices=[('F', 'Fold'), ('X', 'Check'), ('L', 'Limp'), ('C', 'Call'), ('B', 'Bet'), ('R', 'Raise'), ('X/F', 'Check/Fold'), ('X/C', 'Check/Call'), ('X/R', 'Check/Raise'), ('L/F', 'Limp/Fold'), ('L/C', 'Limp/Call'), ('L/R', 'Limp/Raise'), ('C/F', 'Call/Fold'), ('C/C', 'Call/Call'), ('C/R', 'Call/Raise'), ('B/F', 'Bet/Fold'), ('B/C', 'Bet/Call'), ('B/R', 'Bet/Raise'), ('R/F', 'Raise/Fold'), ('R/C', 'Raise/Call'), ('R/R', 'Raise/Raise')], max_length=50, null=True),
        ),
    ]
