# Generated by Django 2.2.5 on 2019-09-25 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20190925_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team', to='core.Team'),
        ),
    ]