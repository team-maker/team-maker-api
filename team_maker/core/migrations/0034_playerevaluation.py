# Generated by Django 2.2.5 on 2019-11-10 16:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_game_team_players_avalailable'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('evaluated_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='core.TeamPlayer')),
                ('evaluator_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performed_evaluations', to='core.TeamPlayer')),
            ],
        ),
    ]
