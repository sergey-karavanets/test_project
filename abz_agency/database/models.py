from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    position = models.CharField(max_length=50)
    employment_date = models.DateField(auto_now_add=False)
    salary = models.PositiveIntegerField()
    employment_photo = models.ImageField(blank=True,
                                         upload_to='images/',
                                         help_text='150x150px',
                                         verbose_name='employment_photo')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return str(self.id) + ' Name: ' + self.name
