# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url
from Recommender import views

urlpatterns = patterns('',
    url(r'^$', views.DataEntry, name='data_entry'),
    url(r'^save_data$', views.SaveData, name='save_data'),
    url(r'^results', views.MainAlgorithm, name='results'),
)