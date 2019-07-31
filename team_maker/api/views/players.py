from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import mixins, generics
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
