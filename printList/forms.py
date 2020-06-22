from django.forms import ModelForm
from django import forms
from .models import Print

class printForm(ModelForm):
    intake_datetime = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Print
        fields = [
            'intake_datetime', 'net_ID', 'email', 'print_name',
            'usage', 'file', 'copies', 'print_Type', 'color',
            'association', 'resolution', 'infill', 'purpose',
            'comment'
        ]

form = printForm()
