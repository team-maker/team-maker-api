from rest_framework.serializers import ModelSerializer
from team_maker.core.models import Player


class RuleSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'description', 'rule_type')
