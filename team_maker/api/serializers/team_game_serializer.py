from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import Game
from team_maker.api.serializers import TeamGroupSerializer


class TeamGameSerializer(ModelSerializer):
    num_goals = SerializerMethodField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'date', 'finished' 'num_goals')

    def get_num_goals(self, instance):
        return instance.goals().count()


class TeamGameDetailedSerializer(ModelSerializer):
    home_team = TeamGroupSerializer(read_only=True)
    away_team = TeamGroupSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'date', 'finished', 'home_team', 'away_team')
