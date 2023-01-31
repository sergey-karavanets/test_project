import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abz_agency.settings')
django.setup()


from faker import Faker
import random
from database.models import Employee


fake = Faker()


class Population:

    def __init__(self, name, position, employment_date, salary):
        if list(Employee.objects.all()) is None:
            self.name = name
            self.position = position
            self.employment_date = employment_date
            self.salary = 200000
            self.parent = None
            Employee.objects.create(name=self.name,
                                    position=self.position,
                                    employment_date=self.employment_date,
                                    salary=self.salary,
                                    parent=None)
            print(f'Create owner {self.name}')
        else:
            self.name = name
            self.position = position
            self.employment_date = employment_date
            self.salary = salary
            self.parent = random.choice(list(Employee.objects.all()))
            if Employee.objects.filter(name=self.name) == self.name:
                self.parent = None
            Employee.objects.create(name=self.name,
                                    position=self.position,
                                    employment_date=self.employment_date,
                                    salary=self.salary,
                                    parent=self.parent)
            print(f'{self.name} employer add to database. Her parent {self.parent}')


def main():
    for _ in range(int(input('How many employees to add to the database?: '))):
        name = fake.name()
        position = fake.job()
        employment_date = fake.date()
        salary = random.randint(100, 1000) * 100
        Population(name, position, employment_date, salary)


if __name__ == '__main__':
    main()