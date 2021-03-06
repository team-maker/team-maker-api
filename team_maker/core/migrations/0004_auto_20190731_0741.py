# Generated by Django 2.1.7 on 2019-07-31 07:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(choices=[('amateur', 'Amateur'), ('federate', 'Federate'), ('semi_professional', 'Semi Professional'), ('professional', 'Professional')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('admin', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_players', to='core.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_players', to='core.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(through='core.TeamPlayer', to='core.Player'),
        ),
    ]
