# Generated by Django 3.0.8 on 2020-07-20 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0004_auto_20200720_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='hand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hand.Hands'),
        ),
    ]
