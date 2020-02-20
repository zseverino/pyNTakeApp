from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('../templates/index.html')
    return HttpResponse(template.render())

def printCheck(request):
    template = loader.get_template('../templates/printCheck.html')
    return HttpResponse(template.render())

def printPrices(request):
    template = loader.get_template('../templates/printPrices.html')
    return HttpResponse(template.render())

def printUpload(request):
    template = loader.get_template('../templates/printUpload.html')
    return HttpResponse(template.render())

def employeeIndex(request):
    template = loader.get_template('../templates/employeeIndex.html')
    return HttpResponse(template.render())