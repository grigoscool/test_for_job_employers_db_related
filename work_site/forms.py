from django.forms import ModelForm
from django import forms

from .models import Director, AssociateDir


class EmployForm(ModelForm):
    # пытался уменьшить количество запросов
    asistent = forms.ModelChoiceField(queryset=AssociateDir.objects, empty_label='choose one')

    # def clean_asistent(self):
    #     asistent_passed = self.cleaned_data.get('asistent')
    #     asistent_include = "BIG BOSS"
    #     if asistent_include in asistent_passed:
    #         return asistent_passed
    #     else:
    #         return forms.ValidationError('"BIG BOSS" have to be in it')

    class Meta:
        model = Director
        fields = '__all__'
