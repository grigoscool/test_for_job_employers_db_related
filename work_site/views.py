from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Director, AssociateDir, Manager, OperatorsKTZ, OperatorsElec, Crawler, Electric
from django.db.models import Q


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
