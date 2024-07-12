from django.urls import path
from .views import get_data, get_another_data

urlpatterns = [
    path('data/', get_data),
    path('another-data/', get_another_data),
]
