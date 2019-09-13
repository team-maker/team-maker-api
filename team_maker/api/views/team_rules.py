from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class TeamRulesView(viewsets.ViewSet,
                    generics.ListAPIView,
                    generics.UpdateAPIView,
                    generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamRule.objects.order_by('-points_amount')  # only users that can access the app
    serializer_class = serializers.TeamRuleSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(team_id=self.kwargs['team_pk'])
        return queryset