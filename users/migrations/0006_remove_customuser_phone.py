# Generated by Django 3.2 on 2022-06-23 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
