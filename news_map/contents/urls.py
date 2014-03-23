from django.conf.urls import patterns, url
from contents import views


urlpatterns = patterns('',
  url(r'^$', views.index_view, name='index'),
  url(r'^news/(?P<total>\d{1,2})/$', views.news_view, name='news'),
)