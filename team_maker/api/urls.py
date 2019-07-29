from django.conf.urls import url
from team_maker.api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^login$', obtain_jwt_token),
    url(r'^facebook-login$', views.FacebookLoginView.as_view(), name='facebook-login')
]
