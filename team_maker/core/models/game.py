from django.db import models


class Game(models.Model):
    team = models.ForeignKey(
        'core.Team',
        null=False,
        related_name='team',
        on_delete=models.CASCADE
    )
    home_team = models.OneToOneField(
        'core.TeamGroup',
        null=True,
        related_name='game_as_home_team',
        on_delete=models.CASCADE
    )
    away_team = models.OneToOneField(
        'core.TeamGroup',
        null=True,
        related_name='game_as_away_team',
        on_delete=models.CASCADE
    )
    date = models.DateField(null=True)
    finished = models.BooleanField(default=False)

    def game_goals(self):
        return self.home_team_goals() | self.away_team_goals()

    def game_mvps(self):
        home_team_mvp = self.home_team.mvp()
        away_team_mvp = self.away_team.mvp()
        if (home_team_mvp.points_amount > away_team_mvp.points_amount):
            return [home_team_mvp]
        elif (away_team_mvp.points_amount > home_team_mvp.points_amount):
            return [away_team_mvp]
        else:
            return [home_team_mvp, away_team_mvp]

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

    def home_team_clean_sheet(self):
        return self.away_team_goals().count() == 0

    def away_team_clean_sheet(self):
        return self.home_team_goals().count() == 0

    def __str__(self):
        return "Game at {} for Team: {}".format(self.date, self.team.name)