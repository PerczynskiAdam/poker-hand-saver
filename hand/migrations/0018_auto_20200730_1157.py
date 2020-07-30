# Generated by Django 3.0.8 on 2020-07-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0017_auto_20200729_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='hands',
            name='flop_1_card',
            field=models.CharField(choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2),
        ),
        migrations.AddField(
            model_name='hands',
            name='flop_1_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hands',
            name='flop_2_card',
            field=models.CharField(choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2),
        ),
        migrations.AddField(
            model_name='hands',
            name='flop_2_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hands',
            name='flop_3_card',
            field=models.CharField(choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2),
        ),
        migrations.AddField(
            model_name='hands',
            name='flop_3_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hands',
            name='river_card',
            field=models.CharField(choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2),
        ),
        migrations.AddField(
            model_name='hands',
            name='river_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hands',
            name='turn_card',
            field=models.CharField(choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2),
        ),
        migrations.AlterField(
            model_name='hands',
            name='turn_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='first_card',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='first_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.CharField(blank=True, choices=[('UTG', 'Under The Gun'), ('MP', 'Middle Position'), ('CO', 'Cut-off'), ('BTN', 'Button'), ('SB', 'Small Blind'), ('BB', 'Big Blind'), ('', 'Choose position')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='second_card',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('J', 'J'), ('T', 'T'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), (' ', 'Card')], default=' ', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='second_card_suit',
            field=models.CharField(blank=True, choices=[('s', 'Spade'), ('h', 'Heart'), ('d', 'Diamond'), ('c', 'Club'), ('x', 'Suit')], default='x', max_length=2, null=True),
        ),
    ]