from django.urls import include, path
from rest_framework import routers
from .views import *


urlpatterns = [
    #path('', include(coll.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('student_list', student_list),
    path('teacher_list', teacher_list)
]
