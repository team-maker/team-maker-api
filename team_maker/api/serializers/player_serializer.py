from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import Player


class PlayerSerializer(ModelSerializer):
    first_name = SerializerMethodField(read_only=True)
    last_name = SerializerMethodField(read_only=True)
    email = SerializerMethodField(read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'rating', 'first_name', 'last_name', 'email')

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_last_name(self, instance):
        return instance.user.last_name

    def get_email(self, instance):
        return instance.user.email
