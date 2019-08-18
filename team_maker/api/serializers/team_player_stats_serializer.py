from rest_framework import serializers
from team_maker.core.models import TeamPlayer
from team_maker.api.serializers import PlayerSerializer


class TeamPlayerStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    goals = serializers.SerializerMethodField(read_only=True)
    goals_conceded = serializers.SerializerMethodField(read_only=True)
    games_played = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = ('id', 'admin', 'points', 'player', 'goals', 'goals_conceded', 'games_played')

    def get_goals(self, instance):
        return 10

    def get_goals_conceded(self, instance):
        return 10

    def get_games_played(self, instance):
        return 15
