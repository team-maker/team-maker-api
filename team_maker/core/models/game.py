from django.db import models


class Game(models.Model):
    team = models.ForeignKey(
        'core.Team',
        null=False,
        related_name='team',
        on_delete=models.CASCADE
    )
    home_team = models.ForeignKey(
        'core.TeamGroup',
        null=True,
        related_name='home_team',
        on_delete=models.CASCADE
    )
    away_team = models.ForeignKey(
        'core.TeamGroup',
        null=True,
        related_name='away_team',
        on_delete=models.CASCADE
    )
    date = models.DateField(null=True)

    def game_goals(self):
        return self.home_team_goals() | self.away_team_goals()

    def home_team_goals(self):
        return self.home_team.goals()

    def away_team_goals(self):
        return self.away_team.goals()

    def winner_team(self):
        home_team_goals = self.home_team.goals().count()
        away_team_goals = self.away_team.goals().count()
        if (home_team_goals > away_team_goals):
            return self.home_team
        elif (away_team_goals > home_team_goals):
            return self.away_team
        else:
            return None

    def __str__(self):
        return "Game at {} for Team: {}".format(self.date, self.team.name)