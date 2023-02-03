from django.forms import ModelForm

from .models import Director


class EmployForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
