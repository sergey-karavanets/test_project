from django.shortcuts import render
from .models import *
from django.db.models import Q


def employee(request):
    data = Employee.objects.all()
    return render(request, 'database/index.html', {'data': data})


def search_results(request):
    data = Employee.objects.filter(
        Q(name__icontains='Smith') | Q(position__icontains='Barrister') | Q(employment_date__icontains='2017') | Q(salary__icontains='61000'))
    return render(request, 'database/search.html', {'data': data})
