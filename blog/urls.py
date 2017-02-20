from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post'),

]
