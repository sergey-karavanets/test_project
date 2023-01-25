from django.shortcuts import render
from .models import *
from django.db.models import Q
from .tree import EmployeeTree


def employee(request):
    data = Employee.objects.all()
    return render(request, 'database/index.html', {'title': 'Employee', 'data': data})


def search_results(request):
    query = request.GET.get('q')
    if query is None:
        data = Employee.objects.all()
    else:
        data = Employee.objects.filter(
            Q(name__icontains=query) |
            Q(position__icontains=query) |
            Q(employment_date__icontains=query) |
            Q(salary__icontains=query))
    return render(request, 'database/search.html', {'title': 'Searching results', 'data': data})


def tree(request):
    data = list(filter(lambda x: x.chief == 'Owner', list(map(lambda x: EmployeeTree(x, Employee.objects.all()), Employee.objects.all()))))
    return render(request, 'database/tree.html', {'title': 'Tree', 'data': data})