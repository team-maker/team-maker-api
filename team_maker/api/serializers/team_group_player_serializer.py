from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField
from team_maker.core.models import TeamGroupPlayer
from team_maker.api.serializers import TeamPlayerSerializer


class TeamGroupPlayerSerializer(ModelSerializer):
    team_player = TeamPlayerSerializer(read_only=True)
    team_group_id = PrimaryKeyRelatedField(read_only=True)
    goals_scored = SerializerMethodField(read_only=True)

    class Meta:
        model = TeamGroupPlayer
        fields = (
            'id',
            'goals_scored',
            'points_amount',
            'team_player',
            'team_group_id'
        )

    def get_goals_scored(self, instance):
        return instance.scored_goals.count()
