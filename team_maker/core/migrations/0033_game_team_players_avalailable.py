# Generated by Django 2.2.5 on 2019-11-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20190926_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='team_players_avalailable',
            field=models.ManyToManyField(through='core.GameAvailablePlayer', to='core.TeamPlayer'),
        ),
    ]
