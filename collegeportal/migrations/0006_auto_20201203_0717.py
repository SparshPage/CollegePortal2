# Generated by Django 3.1.4 on 2020-12-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeportal', '0005_auto_20201203_0653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectattandancetable',
            old_name='count',
            new_name='attended',
        ),
        migrations.AddField(
            model_name='subjectattandancetable',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
