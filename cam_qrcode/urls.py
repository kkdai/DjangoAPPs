from django.conf.urls import patterns, url
 
from cam_qrcode import views
 
urlpatterns = patterns('',
    # ex: /cam_qrcode/
    url(r'^$', views.index, name='index'),
    # ex: /cam_qrcode/5/
    url(r'^(?P<cam_id>\d+)/$', views.detail, name='detail'),
    # ex: /cam_qrcode/5/results/
    url(r'^(?P<cam_id>\d+)/results/$', views.results, name='results'),
    # ex: /cam_qrcode/5/detail/
    url(r'^(?P<cam_id>\d+)/detail/$', views.results, name='detail'),
    # ex: /cam_qrcode/add/
    url(r'^add/$', views.add_cam, name='add_cam'),
)