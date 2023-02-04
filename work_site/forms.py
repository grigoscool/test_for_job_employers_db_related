from django.forms import ModelForm
from django import forms

from .models import Director, AssociateDir


class EmployForm(ModelForm):
    # пытался уменьшить количество запросов
    asistent = forms.ModelChoiceField(queryset=AssociateDir.objects, empty_label='choose one')
    class Meta:
        model = Director
        fields = '__all__'
