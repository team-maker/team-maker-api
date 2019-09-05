# Generated by Django 2.1.7 on 2019-09-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20190901_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamplayer',
            old_name='points',
            new_name='points_total',
        ),
        migrations.AlterField(
            model_name='rule',
            name='rule_type',
            field=models.CharField(choices=[('presence', 'Presence'), ('goal', 'Goal'), ('hattrick', 'Hattrick'), ('goal_conceded', 'Goal Conceded'), ('clean_sheet', 'Clean Sheet'), ('own_goal', 'Own Goal')], max_length=50),
        ),
    ]