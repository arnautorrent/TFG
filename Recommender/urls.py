from django.conf.urls import patterns, url
from Recommender import views

urlpatterns = patterns('',
    url(r'^$', views.DataEntry, name='data_entry'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)