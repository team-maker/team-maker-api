
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('team_maker.api.urls', namespace='api')),
    url(r'^admin/', include('team_maker.admin.urls', namespace='admin')),
]