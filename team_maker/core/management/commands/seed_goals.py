from django.core.management.base import BaseCommand
from random import sample
from team_maker.core import models

teams_list = ['Alverca', 'Beira-Mar', 'Belenenses', 'Benfica', 'Boavista', 'Braga', 'Farense', 'GilVicente', 'Leiria', 'Marítimo', 'P.Ferreira', 'Porto', 'Salgueiros', 'SantaClara', 'Sporting', 'Varzim', 'Vit.Guimarães', 'Vit.Setúbal', 'Académica', 'Aves', 'Campomaiorense', 'Chaves', 'E.Amadora', 'Espinho', 'Felgueiras', 'Leça', 'Maia', 'Moreirense', 'Nacional', 'Naval', 'Oliveirense', 'Ovarense', 'Penafiel', 'Portimonense', 'RioAve', 'U.Lamas', 'BragaB', 'Bragança', 'CanelasGaia', 'Ermesinde', 'Esposende', 'Famalicão', 'Freamunde', 'GondomarSC', 'Infesta', 'Joane', 'Leixões', 'Marco', 'Paredes', 'PedrasRubras', 'PortoB', 'Sandinenses', 'Taipas', 'VilaReal', 'Vilanovense', 'Vizela', 'Ac.Viseu', 'Alcaíns', 'Arrifanense', 'B.C.Branco', 'Beneditense', 'CaldasSC', 'Fátima', 'Feirense', 'Marinhense', 'O.Bairro', 'O.Hospital', 'Odivelas', 'S.J.Ver', 'Sanjoanense', 'Sourense', 'Sp.Covilhã', 'Sp.Pombal', 'Torreense', 'U.Coimbra', 'Vilafranquense', 'Amora', 'Atlético', 'Barreirense', 'BenficaB', 'C.Lobos', 'Camacha', 'CasaPia', 'Estoril', 'Imortal', 'Louletano', 'Lusitânia', 'Machico', 'MarítimoB', 'O.Moscavide', 'Olhanense', 'Operário(POR)', 'Padernense', 'Seixal', 'SportingC.P.B', 'U.Madeira']


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **options):
        # users_count = models.User.objects.count()
        # players_count = models.Player.objects.count()
        # team_players_count = models.TeamPlayer.objects.count()
        # team = self.create_team()        # team = models.Team.objects.last()
        # game = models.Game.objects.create(team=team, date=date.today())
        game = models.Game.objects.last()
        game.goals.all().delete()
        for x in range(5):
            home_scorer = game.home_team.team_group_players.all().order_by('?')[0]
            away_scorer = game.away_team.team_group_players.order_by('?')[0]
            models.Goal.objects.create(
                scorer=home_scorer,
                game=game
            )
            models.Goal.objects.create(
                scorer=away_scorer,
                game=game
            )

        # self.stdout.write("Created Users: {}".format(models.User.objects.count() - users_count))
        # self.stdout.write("Created Players: {}".format(models.Player.objects.count() - players_count))
        # self.stdout.write("Created Team Players: {}".format(models.TeamPlayer.objects.count() - team_players_count))