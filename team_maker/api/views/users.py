from team_maker.core import models
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import status, mixins, generics
from team_maker.api import serializers
from django.utils.crypto import get_random_string


class FacebookLoginView(mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.User.objects  # only users that can access the app
    serializer_class = serializers.UserSerializerWithToken
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.get_queryset()
        obj, created = queryset.get_or_create(email=self.request.data['email'])
        if created:
            obj.set_password(get_random_string())
            obj.save()
        return obj

    def put(self, request, *args, **kwargs):
        request_data = request.data
        names = request_data['name'].split(' ')
        request_data['first_name'] = names[0]
        request_data['last_name'] = names[-1]
        del(request_data['name'])
        del(request_data['image_url'])
        serializer = self.get_serializer(data=request_data)
        updated_instance = serializer.update(self.get_object(), request_data)
        return Response(serializer.to_representation(updated_instance), status=status.HTTP_201_CREATED)
