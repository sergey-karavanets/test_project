from django.db import models
import django_filters


class Employee(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    employment_date = models.DateField(auto_now_add=False)
    salary = models.PositiveIntegerField()
    chief = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'staff'

    def __str__(self):
        return self.name