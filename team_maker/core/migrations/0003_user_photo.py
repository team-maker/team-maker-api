# Generated by Django 2.1.7 on 2019-07-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190716_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]