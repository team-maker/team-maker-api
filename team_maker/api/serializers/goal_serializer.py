from rest_framework.serializers import ModelSerializer
from team_maker.core.models import Goal
from team_maker.api.serializers import TeamGroupPlayerSerializer


class GoalSerializer(ModelSerializer):
    scorer = TeamGroupPlayerSerializer(read_only=False)

    class Meta:
        model = Goal
        fields = ('id', 'scorer', 'own_goal')
