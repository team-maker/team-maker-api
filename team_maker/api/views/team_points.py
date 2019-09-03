from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class TeamPointsView(viewsets.ViewSet,
                     generics.ListAPIView,
                     generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Point.objects.order_by('-points_amount')  # only users that can access the app
    serializer_class = serializers.PointSerializer

