
from django.urls import path
from .views import dashboard, show

urlpatterns = [
    path('dashboard/', dashboard),
    path('show/', show),
]
