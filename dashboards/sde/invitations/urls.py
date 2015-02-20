from django.conf.urls import patterns
from django.conf.urls import url

from .views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^\?tab=mypanel_tabs__tab$', IndexView.as_view(), name='mypanel_tabs'),
)
