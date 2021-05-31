from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('django_101.cities.urls')),
    path('', include('django_101.people.urls')),
]
