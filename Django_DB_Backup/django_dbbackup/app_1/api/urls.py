from django.urls import path
from app_1.api.views import trial

urlpatterns = [
    path('',trial)
]