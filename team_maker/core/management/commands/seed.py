from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from datetime import date
import random
from team_maker.core import models
from team_maker.core import services

teams_list = ['Alverca', 'Beira-Mar', 'Belenenses', 'Benfica', 'Boavista', 'Braga', 'Farense', 'GilVicente', 'Leiria', 'Marítimo', 'P.Ferreira', 'Porto', 'Salgueiros', 'SantaClara', 'Sporting', 'Varzim', 'Vit.Guimarães', 'Vit.Setúbal', 'Académica', 'Aves', 'Campomaiorense', 'Chaves', 'E.Amadora', 'Espinho', 'Felgueiras', 'Leça', 'Maia', 'Moreirense', 'Nacional', 'Naval', 'Oliveirense', 'Ovarense', 'Penafiel', 'Portimonense', 'RioAve', 'U.Lamas', 'BragaB', 'Bragança', 'CanelasGaia', 'Ermesinde', 'Esposende', 'Famalicão', 'Freamunde', 'GondomarSC', 'Infesta', 'Joane', 'Leixões', 'Marco', 'Paredes', 'PedrasRubras', 'PortoB', 'Sandinenses', 'Taipas', 'VilaReal', 'Vilanovense', 'Vizela', 'Ac.Viseu', 'Alcaíns', 'Arrifanense', 'B.C.Branco', 'Beneditense', 'CaldasSC', 'Fátima', 'Feirense', 'Marinhense', 'O.Bairro', 'O.Hospital', 'Odivelas', 'S.J.Ver', 'Sanjoanense', 'Sourense', 'Sp.Covilhã', 'Sp.Pombal', 'Torreense', 'U.Coimbra', 'Vilafranquense', 'Amora', 'Atlético', 'Barreirense', 'BenficaB', 'C.Lobos', 'Camacha', 'CasaPia', 'Estoril', 'Imortal', 'Louletano', 'Lusitânia', 'Machico', 'MarítimoB', 'O.Moscavide', 'Olhanense', 'Operário(POR)', 'Padernense', 'Seixal', 'SportingC.P.B', 'U.Madeira']


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **options):
        # users_count = models.User.objects.count()
        # players_count = models.Player.objects.count()
        # team_players_count = models.TeamPlayer.objects.count()
        # team = self.create_team()
        # for x in range(13):
            # user = self.create_user()
            # player = self.create_player(user.id)
            # self.create_team_player(team, player)
        # team = models.Team.objects.last()
        # game = models.Game.objects.create(team=team, date=date.today())
        game = models.Game.objects.last()
        services.games.generate_balanced_teams(game)
        # self.stdout.write("Created Users: {}".format(models.User.objects.count() - users_count))
        # self.stdout.write("Created Players: {}".format(models.Player.objects.count() - players_count))
        # self.stdout.write("Created Team Players: {}".format(models.TeamPlayer.objects.count() - team_players_count))

    def create_user(self):
        fake = Faker()
        self.stdout.write(fake.email())
        user = models.User.objects.create(
            first_name=fake.first_name_male(),
            last_name=fake.last_name_male(),
            email=fake.email(),
        )
        return user

    def create_player(self, user_id):
        player = models.Player.objects.create(
            user_id=user_id,
            rating=random.randint(1, 11)
        )
        return player

    def create_team(self):
        team = models.Team.objects.create(
            name=random.sample(teams_list, 1)[0]
        )
        return team

    def create_team_player(self, team, player):
        team_player = models.TeamPlayer.objects.create(
            team=team,
            player=player
        )
        return team_player
