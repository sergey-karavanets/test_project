from .models import *


class EmployeeTree:

    def __init__(self, employeer: Employee, allEmployees):
        self.name = employeer.name
        self.position = employeer.position
        self.employment_date = employeer.employment_date
        self.salary = employeer.salary
        self.chief = employeer.chief
        self.children = list(map(lambda x: EmployeeTree(x, allEmployees), allEmployees.filter(chief=self.name)))