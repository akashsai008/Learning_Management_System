from django import forms
from .models import *

class CustomAdminForm(forms.Form):
    video = forms.FileField(label='Upload Video') 
    description = forms.CharField(widget=forms.Textarea, label='Description')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Course', widget=forms.Select)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department', widget=forms.Select)