from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from printList.forms import printForm, updateForm
from printList.models import Print, Printer, Status
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


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


@login_required
def employeeUpdate(request, pk):
        instance = get_object_or_404(Print, pk=pk)
        form = updateForm(request.POST or request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully updated the print!")
            return HttpResponseRedirect('/employeeIndex')
        return render(request, 'employeeIntake.html', {'form': form})

@login_required
def employeeCheck(request, pk):
    instance = get_object_or_404(Print, pk=pk)
    instance.status = Status.objects.get(status_text="Done")
    instance.printer = Printer.objects.get(printer_name="None")
    email = instance.email
    send_mail('3D Print Ready at MAKEmory', 'Dear Customer,\n \nYour 3D printing project has been completed and is ready to be picked up. As a reminder, the only accepted payments are either through Eagle Dollars (on your Emory Card) or speedtypes (for clubs, departments, etc.) \n \n'
                                            'MAKEmory in the Computing Center is open during the following hours:\n'
                                            'Monday - Thursday: noon - 8pm\n'
                                            'Friday: noon - 5pm\n \n'
                                            'Please feel free to stop by at your earliest convenience and someone in MAKEmory will be able to assist you.\n \n'
                                            'Thank you,\n'
                                            'MAKEmory Staff',
              'zackseve@gmail.com', [email], fail_silently=False)
    instance.save()
    return HttpResponseRedirect('/employeeIndex')
