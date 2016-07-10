from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[\w|-|\d]+)/$', views.repository, name='repository'),
    url(r'^(?P<name>[\w|-|\d]+)/(?P<tag>[\w|-|\d|.]+)/$', views.image, name='image'),
]
