# Generated by Django 3.2 on 2022-06-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rank',
            field=models.IntegerField(choices=[(0, 'Master'), (1, 'Senior Officer'), (2, 'Junior Officer'), (3, 'Bosun'), (4, 'Potential User')], default=4),
        ),
    ]
