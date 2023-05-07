from django.urls import path, include
from . import views

# ! Setting application name
app_name = 'login_app'

# ! Setting urls paths
urlpatterns = [
    path('', views.login_page, name = 'login'),
    path('logout/', views.logout_page, name = 'logout')
]
