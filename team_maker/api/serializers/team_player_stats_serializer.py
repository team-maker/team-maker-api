from rest_framework import serializers
from team_maker.core.models import TeamPlayer
from team_maker.api.serializers import PlayerSerializer


class TeamPlayerStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    goals_scored = serializers.SerializerMethodField(read_only=True)
    own_goals = serializers.SerializerMethodField(read_only=True)
    games_played = serializers.SerializerMethodField(read_only=True)
    evaluated_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = (
            'id',
            'admin',
            'points_total',
            'position',
            'player',
            'goals_scored',
            'own_goals',
            'games_played',
            'evaluated_rating'
        )

    def get_goals_scored(self, instance):
        return instance.goals_scored().count()

    def get_own_goals(self, instance):
        return instance.own_goals().count()

    def get_games_played(self, instance):
        return instance.games_played().count()
    
    def get_evaluated_rating(self, instance):
        evaluator_player = self.context['request'].user.player
        team = instance.team
        evaluator_team_player = team.team_players.get(player=evaluator_player)
        evaluation, created = instance.evaluations.get_or_create(
            evaluator_player=evaluator_team_player
        )
        return evaluation.rating
