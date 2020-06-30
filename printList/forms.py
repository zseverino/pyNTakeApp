from django import forms
from django.forms import ModelForm
from .models import Print

class printForm(ModelForm):
    class Meta:
        model = Print

        fields = [
            'net_ID_or_name', 'email', 'association', 'purpose',
            'print_name', 'file', 'printer_file', 'copies', 'usage', 'print_Type', 'color',
            'resolution', 'infill', 'comment', 'verification'
        ]

class updateForm(ModelForm):
    class Meta:
        model = Print
        fields = [
            'file', 'printer_file', 'copies', 'print_Type', 'color',
            'resolution', 'infill', 'usage', 'printer', 'status', 'verification',
            'comment'
        ]

class submitForm(ModelForm):
    class Meta:
        model = Print
        fields = [
            'net_ID_or_name', 'email', 'association', 'purpose',
            'print_name', 'file', 'copies', 'print_Type', 'color',
            'comment'
        ]

class checkForm(forms.Form):
    email = forms.CharField(label='Email', max_length=25)
