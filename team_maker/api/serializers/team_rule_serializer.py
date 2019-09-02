from rest_framework.serializers import ModelSerializer
from team_maker.core.models import Player
from team_maker.api.serializers import RuleSerializer


class TeamRuleSerializer(ModelSerializer):
    rule = RuleSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'points_amount', 'rule')

