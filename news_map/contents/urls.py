from django.conf.urls import patterns, include, url
from contents import views


urlpatterns = patterns('',
  url(r'^$', view.index, name='index'),
)