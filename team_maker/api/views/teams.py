from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import mixins, generics, status
from team_maker.api import serializers


class TeamView(generics.ListCreateAPIView,
               generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Team.objects  # only users that can access the app
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
