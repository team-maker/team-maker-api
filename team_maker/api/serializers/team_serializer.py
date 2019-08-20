from rest_framework.serializers import ModelSerializer
from team_maker.core.models import Team
from team_maker.api.serializers import TeamPlayerSerializer


class TeamSerializer(ModelSerializer):
    team_players = TeamPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'token', 'team_players')
