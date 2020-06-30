from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from printList.forms import printForm, updateForm, submitForm, checkForm
from printList.models import Print, Printer, MailMessage, MailSubjectLine
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
import csv


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
            messages.success(request, "Print Submitted!")
            return HttpResponseRedirect('/')
    else:
        form = submitForm()
    return render(request, 'printUpload.html', {'form': form})


class printCheck(generic.FormView):
    form_class = checkForm
    template_name = 'printCheck.html'

    def form_valid(self, form, **kwargs):
        return self.render_to_response(self.get_context_data(form=form, email=form.data['email'], print_list=Print.objects.all()))

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
            messages.success(request, "You successfully updated the print!")
            return HttpResponseRedirect('/employeeIndex')
    else:
        form = updateForm(instance=instance)
    return render(request, 'employeeIntake.html', {'form': form})


@login_required
def employeeMarkPrinted(request, pk):
    instance = get_object_or_404(Print, pk=pk)
    instance.status = 'PRINTED'
    instance.printer = Printer.objects.get(printer_name="None", print_Type=instance.print_Type)
    email = instance.email
    send_mail(subject=get_object_or_404(MailSubjectLine, pk=1).subject_text, message=get_object_or_404(MailMessage, pk=1).message_text, from_email='zackseve@gmail.com', recipient_list=[email], fail_silently=False)
    instance.save()
    return HttpResponseRedirect('/employeeIndex')

@login_required
def dataExport(request):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = Print.objects.all().model._meta
    model = Print.objects.all().model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=TechLab_Prints.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in Print.objects.all():
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


