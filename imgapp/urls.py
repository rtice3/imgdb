from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'unprocessed', views.unprocessed_img, name='unprocessed'),
    url(r'processed', views.processed_img, name='processed'),
    url(r'^(?P<serial>[0-9]+)/serial_search/$', views.serial_search, name='serial search'),
]