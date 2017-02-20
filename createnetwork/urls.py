from . import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.analysis_list, name='analysis_list'),
#    url(r'', include('createnetwork.urls')),
]
