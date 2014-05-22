from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    #APP: For feed poster
    url(r'^feed_poster/', include('feed_poster.urls')),
    #APP: Test for polls
    url(r'^polls/', include('polls.urls', namespace='polls'))
    #url(r'^admin/', include(admin.site.urls)),
)