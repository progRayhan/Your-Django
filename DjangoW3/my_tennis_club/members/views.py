# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def member(request):
#     return HttpResponse("Hello World!")

def member(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())