from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from printList.forms import printForm
from printList.models import Print

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

@login_required
def employeeIntake(request):
    if request.method == 'POST':
        form = printForm(request.POST, request.FILES)
        if form.is_valid():
            new_print = form.save()
            return HttpResponseRedirect('/employeeIndex')

    else:
        form = printForm()
    return render(request, 'employeeIntake.html', {'form': form})