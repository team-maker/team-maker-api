from django.core.management.base import BaseCommand
from datetime import date
import datetime
from team_maker.core import models
from team_maker.core import services


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **options):
        team = models.Team.objects.get(
            name='Runtime Revolution - Club Football'
        )
        self.create_player(team, 'j.rosa@runtime-revolution.com', 'João', 'Rosa', 5)
        self.create_player(team, 'j.sa@runtime-revolution.com', 'José', 'Sá', 7)
        self.create_player(team, 'm.almeida@runtime-revolution.com', 'Miguel', 'Almeida', 4)
        self.create_player(team, 'r.sebastiao@runtime-revolution.com', 'Rui', 'Sebastião', 8)
        self.create_player(team, 'a.correia@runtime-revolution.com', 'André', 'Correia', 8)
        self.create_player(team, 'a.martins@runtime-revolution.com', 'André', 'Martins', 6)
        self.create_player(team, 'i.pereira@runtime-revolution.com', 'Ivo', 'Pereira', 6)
        self.create_player(team, 't.goncalves@runtime-revolution.com', 'Tiago', 'Gonçalves', 6)
        self.create_player(team, 't.daniel@runtime-revolution.com', 'Tiago', 'Daniel', 8)
        self.create_player(team, 'f.moura@runtime-revolution.com', 'Fred', 'Moura', 6)
        self.create_player(team, 'a.nunes@runtime-revolution.com', 'André', 'Nunes', 7)
        self.create_player(team, 'f.pires@runtime-revolution.com', 'Francisco', 'Pires', 6)
        self.create_player(team, 'r.pinto@runtime-revolution.com', 'Rui', 'Pinto', 5)
        self.create_player(team, 'r.dinis@runtime-revolution.com', 'Rúben', 'Dinis', 9)
        game_date = date.today() + datetime.timedelta(days=1)
        game = models.Game.objects.create(team=team, date=game_date)
        services.games.generate_balanced_teams(game)

    def create_player(self, team, email, first_name, last_name, rating):
        user = models.User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        player = user.player
        player.rating = rating
        player.save()

        models.TeamPlayer.objects.create(
            team=team,
            player=player
        )
