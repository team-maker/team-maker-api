from rest_framework.serializers import ModelSerializer
from team_maker.core.models import TeamRule
from team_maker.api.serializers import RuleSerializer


class TeamRuleSerializer(ModelSerializer):
    rule = RuleSerializer(read_only=True)

    class Meta:
        model = TeamRule
        fields = ('id', 'points_amount', 'rule')

