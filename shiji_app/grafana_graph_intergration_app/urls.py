from  django.urls import path, include
from . import views
from prometheus_client import exposition

app_name = 'grafana_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about')
]
