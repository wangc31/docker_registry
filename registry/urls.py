from django.conf.urls import url

from . import views

REPO_PATTERN = '\w|\-|\d|/|_|.'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[' + REPO_PATTERN + ']+)/$', views.repository, name='repository'),
    url(r'^(?P<name>[' + REPO_PATTERN + ']+)/:(?P<tag>[\w|\-|\d|.|/]+)/$', views.image, name='image'),
]
