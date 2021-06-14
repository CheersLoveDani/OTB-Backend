from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/heroes/', include('heroes.urls')),
    path('api/teams/', include('teams.urls'))
]
