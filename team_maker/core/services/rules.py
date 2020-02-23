from team_maker.core import models


def generate_presence_points(team_rule, game):
    for team_group_player in game.game_team_group_players():
        models.Point.objects.create(
            team_group_player=team_group_player,
            points_amount=team_rule.points_amount,
            description='Points earned by presence',
            team_rule=team_rule
        )


def generate_goal_points(team_rule, game):
    for goal in game.scored_goals():
        models.Point.objects.create(
            team_group_player=goal.scorer,
            points_amount=team_rule.points_amount,
            description='Points earned by goal scored',
            team_rule=team_rule
        )


def generate_hattrick_points(team_rule, game):
    for scorer in game.home_team.hattricks():
        models.Point.objects.create(
            team_group_player=scorer,
            points_amount=team_rule.points_amount,
            description='Points earned by Hattrick scored',
            team_rule=team_rule
        )
    for scorer in game.away_team.hattricks():
        models.Point.objects.create(
            team_group_player=scorer,
            points_amount=team_rule.points_amount,
            description='Points earned by Hattrick scored',
            team_rule=team_rule
        )


def generate_goals_conceded_points(team_rule, game):
    home_team_goals, remainder = divmod(game.home_team_goals().count(), 2)
    if home_team_goals >= 1:
        for team_group_player in game.away_team_group_players():
            models.Point.objects.create(
                team_group_player=team_group_player,
                points_amount=team_rule.points_amount * home_team_goals,
                description='Points subtracted by Team Game Goals Conceded',
                team_rule=team_rule
            )
    away_team_goals, remainder = divmod(game.away_team_goals().count(), 2)
    if away_team_goals >= 1:
        for team_group_player in game.home_team_group_players():
            models.Point.objects.create(
                team_group_player=team_group_player,
                points_amount=team_rule.points_amount * away_team_goals,
                description='Points subtracted by Team Game Goals Conceded',
                team_rule=team_rule
            )


def generate_goals_scored_points(team_rule, game):
    home_team_goals, remainder = divmod(game.home_team_goals().count(), 2)
    if home_team_goals >= 1:
        for team_group_player in game.home_team_group_players():
            models.Point.objects.create(
                team_group_player=team_group_player,
                points_amount=team_rule.points_amount * home_team_goals,
                description='Points earned by Team Game Goals Scored',
                team_rule=team_rule
            )
    away_team_goals, remainder = divmod(game.away_team_goals().count(), 2)
    if away_team_goals >= 1:
        for team_group_player in game.away_team_group_players():
            models.Point.objects.create(
                team_group_player=team_group_player,
                points_amount=team_rule.points_amount * away_team_goals,
                description='Points earned by Team Game Goals Scored',
                team_rule=team_rule
            )


def generate_clean_sheet_points(team_rule, game):
    home_team_clean_sheet = game.home_team_clean_sheet()
    if home_team_clean_sheet:
        for team_group_player in game.home_team_group_players():
            models.Point.objects.create(
                team_group_player=team_group_player,
                points_amount=team_rule.points_amount,
                description='Points earned by Game Clean Sheet',
                team_rule=team_rule
            )
    away_team_clean_sheet = game.away_team_clean_sheet()
    if away_team_clean_sheet:
        for team_group_player in game.away_team_group_players():
            models.Point.objects.create(
                team_group_player=team_group_player,
                points_amount=team_rule.points_amount,
                description='Points earned by Game Clean Sheet',
                team_rule=team_rule
            )


def generate_own_goal_points(team_rule, game):
    for goal in game.own_goals():
        models.Point.objects.create(
            team_group_player=goal.scorer,
            points_amount=team_rule.points_amount,
            description='Points subtracted by own goal scored',
            team_rule=team_rule
        )


def generate_game_victory_points(team_rule, game):
    winner_team = game.winner_team()
    if winner_team is None:
        return
    for team_group_player in winner_team.team_group_players.all():
        models.Point.objects.create(
            team_group_player=team_group_player,
            points_amount=team_rule.points_amount,
            description='Points earned by Game Victory',
            team_rule=team_rule
        )


def generate_game_defeat_points(team_rule, game):
    winner_team = game.winner_team()
    if winner_team is None:
        return

    loser_team = None
    if(winner_team == game.away_team):
        loser_team = game.home_team
    else:
        loser_team = game.away_team

    for team_group_player in loser_team.team_group_players.all():
        models.Point.objects.create(
            team_group_player=team_group_player,
            points_amount=team_rule.points_amount,
            description='Points subtracted by Game Defeat',
            team_rule=team_rule
        )


def generate_game_mvp_points(team_rule, game):
    for mvp in game.game_mvps():
        models.Point.objects.create(
            team_group_player=mvp,
            points_amount=team_rule.points_amount,
            description='Points earned by being game MVP',
            team_rule=team_rule
        )


def rule_type_to_function(rule_type):
    rules_switch = {
        'presence': generate_presence_points,
        'goal': generate_goal_points,
        'hattrick': generate_hattrick_points,
        'goals_conceded': generate_goals_conceded_points,
        'goals_scored': generate_goals_scored_points,
        'clean_sheet': generate_clean_sheet_points,
        'own_goal': generate_own_goal_points,
        'game_victory': generate_game_victory_points,
        'game_defeat': generate_game_defeat_points
    }
    return rules_switch.get(rule_type, lambda: "nothing")


def generate_rule_points(team_rule, game):
    func = rule_type_to_function(team_rule.rule.rule_type)
    return func(team_rule, game)
