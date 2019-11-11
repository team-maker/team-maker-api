from team_maker.core import models
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics, status
from team_maker.api.serializers import EvaluationSerializer


class TeamPlayerEvaluationView(generics.UpdateAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.PlayerEvaluation.objects
    serializer_class = EvaluationSerializer

    def put(self, request, *args, **kwargs):
        player_evaluation = self.get_object()
        player_evaluation.rating = self.request.data['rating']
        try:
             player_evaluation.full_clean()
        except ValidationError as e:
            return Response(str(e.messages).strip('[]').replace('\'', ''), status=status.HTTP_400_BAD_REQUEST)
       
        player_evaluation.save()
        return Response(status=status.HTTP_200_OK)