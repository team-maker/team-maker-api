from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import Team
from team_maker.api.serializers import TeamPlayerSerializer


class TeamSerializer(ModelSerializer):
    team_players = SerializerMethodField(read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'token', 'team_players')

    def get_team_players(self, instance):
        team_players = instance.team_players.order_by('-points_total')
        return TeamPlayerSerializer(team_players, many=True).data
