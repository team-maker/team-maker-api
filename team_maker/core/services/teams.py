OWN_RATING_WEIGHT = 0.8
CURRENT_POINTS_WEIGHT = 0.2


def generate_balanced_teams(team):
    # team = game.team
    team_players = team.team_players.all()
    player_values = []
    for team_player in team_players:
        value = team_player.player.rating * OWN_RATING_WEIGHT + team_player.points * CURRENT_POINTS_WEIGHT
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
    print(home_value)
    print(away_value)