from . import views
from django.conf.urls import include, url
from django.contrib import admin
# from createnetwork.views import NetworkCommandPage

urlpatterns = [
    url(r'^$', views.analysis_list, name='analysis_list'),
    url(r'^makecommand/$',views.NetworkCommandPage.as_view()),
    ]

#urlpatterns = [
#    url(r'^$', views.analysis_list, name='analysis_list'),
#    url(r'', include('createnetwork.urls')),
    
#]

