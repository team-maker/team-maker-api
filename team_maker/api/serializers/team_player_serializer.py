from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from team_maker.core.models import TeamPlayer
from team_maker.api.serializers import PlayerSerializer


class TeamPlayerSerializer(ModelSerializer):
    player = PlayerSerializer(read_only=True)
    team_id = PrimaryKeyRelatedField(read_only=True)
    goals_scored = SerializerMethodField(read_only=True)
    games_played = SerializerMethodField(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = (
            'id',
            'admin',
            'points_total',
            'goals_scored',
            'games_played',
            'player',
            'team_id'
        )

    def get_goals_scored(self, instance):
        return instance.goals_scored().count()

    def get_games_played(self, instance):
        return instance.games_played().count()

