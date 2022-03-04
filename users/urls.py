from django.urls import path
from .views import TestAPIView


urlpatterns = [
    path('info/', TestAPIView.as_view())
]
