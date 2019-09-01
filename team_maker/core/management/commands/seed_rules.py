from django.core.management.base import BaseCommand, CommandError
from team_maker.core import models

class Command(BaseCommand):
    help = 'Seed database with rules'

    def handle(self, *args, **options):
        models.Rule.objects.create(
            description='Number of points for each game presence',
            rule_type='presence',
            default_points=1
        )
        models.Rule.objects.create(
            description='Number of points for each goal scored',
            rule_type='goal',
            default_points=5
        )
        models.Rule.objects.create(
            description='Number of points for each hattrick scored',
            rule_type='goal',
            default_points=10
        )
        models.Rule.objects.create(
            description='Number of points to subtract for each goal conceded by the team',
            rule_type='goal_conceded',
            default_points=1
        )
        models.Rule.objects.create(
            description='Number of points for each game without goals conceded',
            rule_type='clean_sheet',
            default_points=3
        )
        models.Rule.objects.create(
            description='Number of points to subtract for each own goal scored',
            rule_type='own_goal',
            default_points=5
        )
