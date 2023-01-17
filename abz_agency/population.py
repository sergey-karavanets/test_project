import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abz_agency.settings')
django.setup()


from faker import Faker
import random
from database.models import Employee


fake = Faker()


def population(value):
    for i in range(value):
        name = fake.name()
        position = fake.job()
        employment_date = fake.date()
        salary = random.randint(100, 1000) * 100
        obj = Employee.objects.create(name=name, position=position, employment_date=employment_date, salary=salary)
        print(f'{value} employees have been added to the database')


def main():
    temp = int(input('How many employees to add to the database? '))
    population(temp)


if __name__ == '__main__':
    main()