from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serialize):
    class Meta:
        fields = '__all__'


class TeacherSerializer(serializer.Serialize):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = user
        fields = '__all__'


class StudentSerializer(serializer.Serialize):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = user
        fields = '__all__'
