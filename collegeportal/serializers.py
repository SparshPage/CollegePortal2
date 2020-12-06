from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Teacher
        fields = [
            "user",
            "name"
        ]

    def create(self, validated_data):
        user = validated_data.pop('user')
        print(user)
        user = User.objects.create(**user)
        teacher = Teacher.objects.create(**validated_data, user=user)

        return teacher


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Student
        fields = [
            'user',
            'name',
            'dob',
            'sex',
            'div',
            'course'
        ]

    def create(self, validated_data):
        user = validated_data.pop('user')
        #course = validated_data.pop('course')

        user = User.objects.create(**user)
        #course = Course.objects.get(pk=course.pk)
        student = Student.objects.create(
            **validated_data, user = user)
        return student

