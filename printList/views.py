from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from printList.forms import printForm, updateForm, submitForm, checkForm
from printList.models import Print, Printer
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


# Create your views here.
def index(request):
    template = loader.get_template('../templates/index.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('../templates/registration/login.html')
    return HttpResponse(template.render())


class employeeIndex(LoginRequiredMixin, generic.ListView):
    model = Print
    template_name = 'employeeIndex.html'


class employeeVerifyIndex(LoginRequiredMixin, generic.ListView):
    model = Print
    template_name = 'employeeVerifyIndex.html'


def printUpload(request):
    if request.method == 'POST':
        form = submitForm(request.POST, request.FILES)
        if form.is_valid():
            new_print = form.save()
            return HttpResponseRedirect('/')
    else:
        form = submitForm()
    return render(request, 'printUpload.html', {'form': form})


class printCheck(generic.FormView):
    form_class = checkForm
    template_name = 'printCheck.html'

    def form_valid(self, form, **kwargs):
        return self.render_to_response(self.get_context_data(form=form, net_id=form.data['net_id'], print_list=Print.objects.all()))


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
def employeeDownload(request, pk):
    instance = get_object_or_404(Print, pk=pk)
    filename = instance.file.name.split('/')[-1]
    response = HttpResponse(instance.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

@login_required
def employeeUpdate(request, pk):
    instance = get_object_or_404(Print, pk=pk)
    if request.method == 'POST':
        form = updateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            new_print = form.save()
            return HttpResponseRedirect('/employeeIndex')
    else:
        form = updateForm(instance=instance)
    return render(request, 'employeeIntake.html', {'form': form})


@login_required
def employeeMarkPrinted(request, pk):
    instance = get_object_or_404(Print, pk=pk)
    instance.status = 'PRINTED'
    instance.printer = Printer.objects.get(printer_name="None")
    email = instance.email
    send_mail('3D Print Ready at MAKEmory',
              'Dear Customer,\n \nYour 3D printing project has been completed and is ready to be picked up. As a reminder, the only accepted payments are either through Eagle Dollars (on your Emory Card) or speedtypes (for clubs, departments, etc.) \n \n'
              'MAKEmory in the Computing Center is open during the following hours:\n'
              'Monday - Thursday: noon - 8pm\n'
              'Friday: noon - 5pm\n \n'
              'Please feel free to stop by at your earliest convenience and someone in MAKEmory will be able to assist you.\n \n'
              'Thank you,\n'
              'MAKEmory Staff',
              'zackseve@gmail.com', [email], fail_silently=True)
    instance.save()
    return HttpResponseRedirect('/employeeIndex')
