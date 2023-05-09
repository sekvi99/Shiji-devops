from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ! admin - django application
    path('admin/', admin.site.urls),
    
    # ! Own applications
    path('login/', include('login_app.urls')),
    path('', include('grafana_graph_intergration_app.urls')),
    
    # ! Prometheus - accesss via base_url/metrics
    path('', include('django_prometheus.urls')),
]
