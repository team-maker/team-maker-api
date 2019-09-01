from rest_framework.serializers import ModelSerializer
from team_maker.core.models import TeamGroup
from team_maker.api.serializers import TeamGroupPlayerSerializer


class TeamGroupSerializer(ModelSerializer):
    team_group_players = TeamGroupPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = TeamGroup
        fields = ('id', 'number_of_players', 'calculated_ponderation', 'team_group_players')