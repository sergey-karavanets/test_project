from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def employee(request):
    data = Employee.objects.all()
    return render(request, 'database/index.html', {'title': 'Employee information',
                                                   'data': data})


@login_required
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
    return render(request, 'database/search.html', {'title': 'Searching results',
                                                    'data': data})


@login_required
def tree(request):
    return render(request, "database/tree.html", {'title': 'Employee Tree',
                                                  'employees': Employee.objects.all()})