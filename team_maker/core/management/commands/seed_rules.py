from django.core.management.base import BaseCommand
from team_maker.core import models


class Command(BaseCommand):
    help = 'Seed database with rules'

    def handle(self, *args, **options):
        models.Rule.objects.get_or_create(
            description='Number of points for each game presence',
            rule_type='presence',
            default_points=1
        )
        models.Rule.objects.get_or_create(
            description='Number of points for each game victory',
            rule_type='game_victory',
            default_points=3
        )
        models.Rule.objects.get_or_create(
            description='Number of points to subtract for each game defeat',
            rule_type='game_defeat',
            default_points=-2
        )
        models.Rule.objects.get_or_create(
            description='Number of points for each goal scored',
            rule_type='goal',
            default_points=4
        )
        models.Rule.objects.get_or_create(
            description='Number of extra points for each hattrick scored',
            rule_type='hattrick',
            default_points=8
        )
        models.Rule.objects.get_or_create(
            description='Number of points to subtract for each 2 goals conceded by the team',
            rule_type='goals_conceded',
            default_points=-1
        )
        models.Rule.objects.get_or_create(
            description='Number of points for each 2 goals scored by the team',
            rule_type='goals_scored',
            default_points=1
        )
        models.Rule.objects.get_or_create(
            description='Number of points for each game without goals conceded',
            rule_type='clean_sheet',
            default_points=3
        )
        models.Rule.objects.get_or_create(
            description='Number of points to subtract for each own goal scored',
            rule_type='own_goal',
            default_points=-4
        )
        models.Rule.objects.get_or_create(
            description='Number of extra points added to the player with more points',
            rule_type='game_mvp',
            default_points=10
        )

