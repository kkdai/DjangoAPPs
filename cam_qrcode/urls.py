from django.conf.urls import patterns, url
 
from cam_qrcode import views
 
urlpatterns = patterns('',
    # ex: /cam_qrcode/
    url(r'^$', views.index, name='index'),
    # ex: /cam_qrcode/5/
    url(r'^(?P<cam_id>\d+)/$', views.detail, name='detail'),
    # ex: /cam_qrcode/5/json
    url(r'^(?P<cam_id>\d+)/json/$', views.json, name='json'),
    # ex: /cam_qrcode/add/
    url(r'^add/$', views.add, name='add'),
    # ex: /cam_qrcode/add_cam/
    url(r'^add_cam/$', views.add_cam, name='add_cam')
)