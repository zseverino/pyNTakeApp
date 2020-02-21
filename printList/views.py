from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

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

def employeeIndex(request):
    num_Prints = Print.objects.all().count()

    return render(request, 'employeeIndex.html')