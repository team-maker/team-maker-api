from rest_framework import serializers
from team_maker.core.models import TeamPlayer
from team_maker.api.serializers import PlayerSerializer


class TeamPlayerStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    goals_scored = serializers.SerializerMethodField(read_only=True)
    own_goals = serializers.SerializerMethodField(read_only=True)
    games_played = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = ('id', 'admin', 'points_total', 'player', 'goals_scored', 'own_goals', 'games_played')

    def get_goals_scored(self, instance):
        return instance.goals_scored().count()

    def get_own_goals(self, instance):
        return instance.own_goals().count()

    def get_games_played(self, instance):
        return instance.games_played().count()
