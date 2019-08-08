from rest_framework.serializers import ModelSerializer
from team_maker.core.models import Team
from team_maker.api.serializers import PlayerSerializer


class TeamSerializer(ModelSerializer):
    players = PlayerSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'players')
