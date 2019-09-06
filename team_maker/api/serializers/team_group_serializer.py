from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import TeamGroup
from team_maker.api.serializers import TeamGroupPlayerSerializer


class TeamGroupSerializer(ModelSerializer):
    team_group_players = TeamGroupPlayerSerializer(many=True, read_only=True)
    goals = SerializerMethodField(read_only=True)

    class Meta:
        model = TeamGroup
        fields = ('id', 'number_of_players', 'calculated_ponderation', 'goals','team_group_players')

    def get_goals(self, instance):
        return instance.goals().count()