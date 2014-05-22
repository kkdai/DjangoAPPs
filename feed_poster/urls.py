from django.conf.urls import patterns, url
 
from feed_poster import views
 
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^feed_get', views.feed_get, name='index'),
)