# Generated by Django 2.1.7 on 2019-08-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190803_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='token',
            field=models.CharField(default='TaWuxT8ZAOWMtcF', max_length=40, unique=True),
        ),
    ]
