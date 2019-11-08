from team_maker.core import models
from django.db.models import Q
from .rules import generate_rule_points, generate_game_mvp_points

OWN_RATING_WEIGHT = 0.8
CURRENT_POINTS_WEIGHT = 0.2


def generate_balanced_teams(game):
    team = game.team
    game_available_players = game.available_players.filter(availability='going').all()
    player_values = []
    for game_team_player in game_available_players:
        team_player = game_team_player.team_player
        value = team_player.player.rating * OWN_RATING_WEIGHT + team_player.points_total * CURRENT_POINTS_WEIGHT
        player_values.append({'team_player': team_player, 'value': value})
    player_values.sort(key=lambda i: i['value'], reverse=True)
    home_team = []
    away_team = []
    for num, player_value in enumerate(player_values):
        if num % 2 == 0:
            home_team.append(player_value)
        else:
            away_team.append(player_value)
    home_value = sum([item['value'] for item in home_team])
    away_value = sum([item['value'] for item in away_team])

    if not game.home_team:
        game.home_team = models.TeamGroup.objects.create(
            game=game,
            calculated_ponderation=home_value,
            number_of_players=len(home_team),
            team=team
        )
    else:
        game.home_team.calculated_ponderation = home_value
        game.home_team.number_of_players = len(home_team)
        game.home_team.team_group_players.all().delete()
        game.home_team.save()

    if not game.away_team:
        game.away_team = models.TeamGroup.objects.create(
            game=game,
            calculated_ponderation=away_value,
            number_of_players=len(away_team),
            team=team
        )
    else:
        game.away_team.calculated_ponderation = home_value
        game.away_team.number_of_players = len(away_team)
        game.away_team.team_group_players.all().delete()
        game.away_team.save()

    game.save()
    for player_value in home_team:
        game.home_team.team_group_players.create(team_player=player_value['team_player'])
    for player_value in away_team:
        game.away_team.team_group_players.create(team_player=player_value['team_player'])


def distribute_game_points(game):
    team = game.team
    team_rules = models.TeamRule.objects.filter(team=team)
    for team_rule in team_rules.filter(~Q(rule__rule_type='game_mvp')):
        generate_rule_points(team_rule, game)
    mvp_rule = team_rules.get(rule__rule_type='game_mvp')
    generate_game_mvp_points(mvp_rule, game)  
    for team_group_player in game.game_team_group_players():
        team_group_player.recalculate_points_amount()
        team_group_player.team_player.recalculate_points_amount()
    position = 1
    for team_player in team.team_players.order_by('-points_total'):
        team_player.position = position
        team_player.save()
        position += 1

    