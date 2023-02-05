from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Director, AssociateDir, Manager, OperatorsKTZ, OperatorsElec, Crawler, Electric
from .forms import EmployForm
from .serializers import DirectorSerialize


def home(request):
    directors = Director.objects.filter(pk__range=(1, 2))
    asis = AssociateDir.objects.filter(pk__range=(1, 4))
    manager = Manager.objects.filter(pk__range=(1, 4))
    operktz = OperatorsKTZ.objects.filter(pk__range=(1, 4))
    operelec = OperatorsElec.objects.filter(pk__range=(1, 4))
    crawler = Crawler.objects.filter(pk__range=(1, 4))
    elec = Electric.objects.filter(pk__range=(1, 4))

    context = {
        'directors': directors,
        'asis': asis,
        'manager': manager,
        'operktz': operktz,
        'operelec': operelec,
        'crawler': crawler,
        'elec': elec,
    }
    return render(request, 'work_site/index.html', context)


@login_required
def show_employ(request):
    directors = Director.objects.all().order_by('-salary')
    context = {
        'directors': directors,
    }
    return render(request, 'work_site/employers.html', context)


@login_required
def search(request):
    searching_data = request.GET.get('search')
    employer = Director.objects.filter(
        Q(fio__icontains=searching_data) | Q(job__icontains=searching_data) | Q(salary__icontains=searching_data))
    context = {
        'employer': employer,
    }
    return render(request, 'work_site/search_results.html', context)


class AddEmployer(CreateView):
    form_class = EmployForm
    template_name = 'work_site/add_employ.html'
    context_object_name = 'form'
    success_url = reverse_lazy('site:employ_list')


class EditEmploy(UpdateView):
    model = Director
    fields = '__all__'
    template_name = 'work_site/edit_employ.html'
    success_url = reverse_lazy('site:employ_list')

    # def get_queryset(self):
    #     return Director.objects.all().select_related('asistent')


def delete_employ(request, pk):
    employer = Director.objects.get(pk=pk)
    employer.delete()
    return redirect('site:employ_list')


class ListDirectors(APIView):
    def get(self, request):
        queryset = Director.objects.all()
        serialized_queryset = DirectorSerialize(instance=queryset, many=True)
        return Response(serialized_queryset.data)
