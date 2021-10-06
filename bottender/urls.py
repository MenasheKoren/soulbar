from django.conf.urls import url
from django.contrib import admin
from bottender.views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]