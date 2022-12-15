from dataclasses import field, fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from summaryapp.models import AssingmentModel, ServiceModel, BarberModel


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AssignmentForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=BarberModel.objects.all(), empty_label="Choose Barber", widget=forms.Select(attrs={'class':'form-control'}))
    service = forms.ModelChoiceField(queryset=ServiceModel.objects.all(), empty_label="Choose Service", widget=forms.Select(attrs={'class':'form-control'}))
    tip = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = AssingmentModel
        fields = ["employee", "service", "tip"]

class ServiceFrom(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # duration = forms.DurationField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # prize = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = ServiceModel
        fields ='__all__'

class BarberFrom(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = BarberModel
        fields = '__all__'