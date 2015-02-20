from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^tfg/', include('Recommender.urls', namespace="Recommender")),
    url(r'^admin/', include(admin.site.urls)),
)
