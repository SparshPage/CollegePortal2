# Generated by Django 3.1.4 on 2020-12-04 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeportal', '0006_auto_20201203_0717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentattendancetable',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='studentattendancetable',
            name='subject6',
        ),
    ]
