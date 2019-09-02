from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import Rule


class RuleSerializer(ModelSerializer):
    rule_type = SerializerMethodField()

    class Meta:
        model = Rule
        fields = ('id', 'description', 'rule_type')

    def get_rule_type(self, instance):
        return instance.get_rule_type_display()