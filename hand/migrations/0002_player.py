# Generated by Django 3.0.8 on 2020-07-20 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero', models.BooleanField(default=False, null=True)),
                ('position', models.CharField(blank=True, choices=[('UTG', 'Under The Gun'), ('MP', 'Middle Position'), ('CO', 'Cut-off'), ('BTN', 'Button'), ('SB', 'Small Blind'), ('BB', 'Big Blind')], max_length=50, null=True)),
                ('first_card', models.CharField(blank=True, choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J')], max_length=10, null=True)),
                ('second_card', models.CharField(blank=True, choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J')], max_length=10, null=True)),
                ('pre_action', models.CharField(blank=True, choices=[('Raise', 'raise'), ('Fold', 'fold'), ('Call', 'call'), ('Check', 'check')], max_length=50, null=True)),
                ('flop_action', models.CharField(blank=True, choices=[('Raise', 'raise'), ('Fold', 'fold'), ('Call', 'call'), ('Check', 'check'), ('Check/Fold', 'checkfold'), ('Bet', 'bet')], max_length=50, null=True)),
                ('pre_act_amount', models.CharField(blank=True, default='', max_length=50)),
                ('flop_act_amount', models.CharField(blank=True, default='', max_length=50)),
                ('hand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hand.Hands')),
            ],
        ),
    ]
