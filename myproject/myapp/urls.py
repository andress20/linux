from django.conf.urls import patterns, url
 
from myapp.views import HomePageView
 
urlpatterns = patterns(
    '',
 
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'home/^$', HomePageView.home),
)