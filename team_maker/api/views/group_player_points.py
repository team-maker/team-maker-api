from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class GroupPlayerPointsView(generics.RetrieveAPIView,
                            generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamGroupPlayer.objects
    serializer_class = serializers.TeamGroupPlayerWithPointsSerializer
