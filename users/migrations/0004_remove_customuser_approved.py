# Generated by Django 3.2 on 2022-06-19 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='approved',
        ),
    ]
