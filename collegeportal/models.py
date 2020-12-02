from django.db import models

# Create your models here.

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class User(User):
    def __str__(self):
        return self.username


class Teacher(models.Model):
    #Teacher_id = models.CharField(max_length=10, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    #subject_id = models.CharField(max_length=10, default="")
    sname = models.CharField(max_length=50, default="")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # scode = models.CharField()

    def __str__(self):
        return self.sname


class Course(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)

    def __str__(self):
        return self.abbr


class SubjectAttandanceTable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class StudentAttendanceTable(models.Model):
    subject1 = models.OneToOneField(
        SubjectAttandanceTable, related_name='subject1', on_delete=models.CASCADE)
    subject2 = models.OneToOneField(
        SubjectAttandanceTable, related_name='subject2', on_delete=models.CASCADE)
    subject3 = models.OneToOneField(
        SubjectAttandanceTable, related_name='subject3', on_delete=models.CASCADE)
    subject4 = models.OneToOneField(
        SubjectAttandanceTable, related_name='subject4', on_delete=models.CASCADE)
    subject5 = models.OneToOneField(
        SubjectAttandanceTable, related_name='subject5', on_delete=models.CASCADE)
    subject6 = models.OneToOneField(
        SubjectAttandanceTable, related_name='subject6', on_delete=models.CASCADE)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.FileField()
    dob = models.DateField(default='1998-01-01')
    sex = models.CharField(max_length=40, choices=(
        ('M', 'M'), ('F', 'F'), ('OTH', 'OTH')), default='M')
    div = models.CharField(max_length=40,
                           choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), default='A')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance = models.OneToOneField(
        StudentAttendanceTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
