# Generated by Django 4.1.5 on 2023-02-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employment_photo',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/', verbose_name='employment_photo'),
        ),
    ]