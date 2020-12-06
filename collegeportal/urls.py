from django.urls import include, path
from rest_framework import routers
from .views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path('', include(coll.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('user_registration/', csrf_exempt(user_registration)),
    #path('register_teacher/', csrf_exempt(register_teacher)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('get_user_by_email/<str:email>', get_user_by_email),
    path('add_teacher/', csrf_exempt(add_teacher)),
    path('student_registration/', csrf_exempt(student_registration))
]
