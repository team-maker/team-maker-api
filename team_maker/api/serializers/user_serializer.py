from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from team_maker.core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserSerializerWithToken(serializers.Serializer):

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
