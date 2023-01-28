from django.http import HttpResponse
from django.urls import path

def help(request):
    return HttpResponse("hello World!")

urlpatterns = [
    path('',help)
]