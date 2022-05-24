from django.forms import ModelForm
from django import forms
from .models import Datepicker


class DatepickerForm(ModelForm):
    name = forms.CharField(required=False)
    dob = forms.DateField(required=False)

    class Meta:
        model = Datepicker
        fields = ['name', 'dob']
