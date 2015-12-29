from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mreq>\w+)!(?P<match>\w+)!(?P<qtype>\w*)=(?P<param>[^!]*)!(?P<sort>-?\w*)$', views.db_query, name='db_query'),
]
