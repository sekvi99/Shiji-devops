from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login_app.urls')),
    path('', include('grafana_graph_intergration_app.urls'))
]
