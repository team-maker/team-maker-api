# Generated by Django 2.1.7 on 2019-08-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_team_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='team',
            name='token',
            field=models.CharField(default='3NKNhIlyRU2rUuB', max_length=40, unique=True),
        ),
    ]
