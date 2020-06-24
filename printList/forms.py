from django import forms
from django.forms import ModelForm
from .models import Print

class printForm(ModelForm):
    class Meta:
        model = Print
        fields = [
            'net_ID_or_name', 'email', 'association', 'purpose',
            'print_name', 'file', 'copies', 'usage', 'print_Type', 'color',
            'resolution', 'infill', 'comment', 'verification'
        ]

class updateForm(ModelForm):
    class Meta:
        model = Print
        fields = [
            'usage', 'file', 'copies', 'print_Type', 'color',
            'resolution', 'infill', 'printer', 'status', 'verification',
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
    net_id = forms.CharField(label='NetID', max_length=10)
