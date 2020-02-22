from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from printList.models import Print, Printer, PrintType, Purpose, Color, Association, Resolution, Infill, Status

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

def login(request):
    template = loader.get_template('../templates/registration/login.html')
    return HttpResponse(template.render())

class employeeIndex(LoginRequiredMixin, generic.ListView):
    model = Print
    template_name = 'employeeIndex.html'