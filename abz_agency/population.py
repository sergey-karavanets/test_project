import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abz_agency.settings')
django.setup()


import shutil
import string
from faker import Faker
import random
from database.models import Employee


photo_name = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']
letters = string.ascii_letters
fake = Faker()


class Population:

    def __init__(self, name, position, employment_date, salary, employment_photo):
        if len(Employee.objects.all()) == 0:
            self.name = name
            self.position = position
            self.employment_date = employment_date
            self.salary = 200000
            self.employment_photo = employment_photo
            self.parent = None
            Employee.objects.create(name=self.name,
                                    position=self.position,
                                    employment_date=self.employment_date,
                                    salary=self.salary,
                                    employment_photo=self.employment_photo,
                                    parent=None)
            print(f'Create owner {self.name}')
        else:
            self.name = name
            self.position = position
            self.employment_date = employment_date
            self.salary = salary
            self.employment_photo = employment_photo
            self.parent = random.choice(list(Employee.objects.all()))
            if Employee.objects.filter(name=self.name) == self.name:
                self.parent = None
            Employee.objects.create(name=self.name,
                                    position=self.position,
                                    employment_date=self.employment_date,
                                    salary=self.salary,
                                    employment_photo=self.employment_photo,
                                    parent=self.parent)
            print(f'{self.name} employer add to database. Her parent {self.parent.name}')


def main():
    for _ in range(int(input('How many employees to add to the database?: '))):
        name = fake.name()
        position = fake.job()
        if len(position) > 50:
            position = position[:50]
        employment_date = fake.date()
        salary = random.randint(100, 1000) * 100
        random_photo = random.choice(photo_name)
        random_letters = ''.join(random.choice(letters) for i in range(10))
        original_photo = 'media/avatars/' + random_photo + '.jpg'
        target = 'media/images/' + random_photo + '_' + random_letters + '.jpg'
        employment_photo = target.replace('media/', '')
        shutil.copyfile(original_photo, target)
        Population(name, position, employment_date, salary, employment_photo)


if __name__ == '__main__':
    main()