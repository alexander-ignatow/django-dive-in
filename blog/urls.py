from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^feed', views.feed, name='feed'),
    url(r'^post/(?P<pkey>[0-9]+)/$', views.post, name='post'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
