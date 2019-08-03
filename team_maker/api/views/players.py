from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import mixins, generics, status
from team_maker.api import serializers


class PlayersView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Player.objects  # only users that can access the app
    serializer_class = serializers.PlayerSerializer

    def get_object(self):
        user = self.request.user
        obj, created = self.queryset.get_or_create(user_id=user.id)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        player = self.get_object()
        user = player.user
        user_data = request.data['user']
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
        player_data = request.data['player']
        player_serializer = self.get_serializer(data=player_data)
        player_serializer.update(player, player_data)
        return Response(status=status.HTTP_204_NO_CONTENT)
