
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import *
#from django.contrib.auth.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
#from django.utils.decorators import method_decorator


def user_registration(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            print(JsonResponse(serializer.errors, status=400))
            return JsonResponse(serializer.errors, status=400)


# Add Teacher
def get_user_by_email(request, email):
    if request.method == 'GET':
        print('fetching request')
        user = User.objects.get(email=email)
        serializer = UserSerializer(user, many=False)
        print('if this prints gg')
        return JsonResponse(serializer.data)


def add_teacher(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # user = User.objects.get(id=pk)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            # serializer.validated_data.user = UserSerializer(user)
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            print(JsonResponse(serializer.errors, status=400))
            return JsonResponse(serializer.errors, status=400)


# @permission_classes((IsAuthenticated,))
def student_registration(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            print(JsonResponse(serializer.errors, status=400))
            return JsonResponse(serializer.errors, status=400)


def student_update_information(request, slug):
    try:
        student = Student.objects.get(slug)

    except student.DoesNotExist:
        return JsonResponse('Object not found', status=400)

    if request.method == 'PUT':
        n
# select Subjects:


def student_select_subjects(request):
    if request.method == 'PUT':
        pass
