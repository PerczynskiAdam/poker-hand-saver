# Generated by Django 3.0.8 on 2020-07-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blinds', models.CharField(choices=[('1/2', '1/2'), ('2/5', '2/5')], default='1/2', max_length=10)),
                ('num_of_players', models.IntegerField()),
                ('publish_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
