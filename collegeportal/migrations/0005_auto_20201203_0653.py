# Generated by Django 3.1.4 on 2020-12-03 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeportal', '0004_auto_20201203_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeportal.studentattendancetable'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
