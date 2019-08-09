from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_jwt.settings import api_settings
from team_maker.core.models import User
from team_maker.api.serializers import PlayerSerializer


class UserSerializer(ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'player')

    def update(self, instance, validated_data):
        if 'player' in validated_data:
            nested_serializer = self.fields['player']
            nested_instance = instance.player
            # note the data is `pop`ed
            nested_data = validated_data.pop('player')
            nested_serializer.update(nested_instance, nested_data)
        return super(UserSerializer, self).update(instance, validated_data)


class UserSerializerWithToken(Serializer):

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def update(self, instance, data):
        for key, value in data.items():
            if not instance._meta.get_field(key):
                setattr(instance, key, value)
        instance.save()
        return instance

    def to_representation(self, user):
        return {
            'token': self.get_token(user),
            'user': UserSerializer(user).data
        }
