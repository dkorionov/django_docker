from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import APIUserRegister

urlpatterns = [
    path(r'registration/', APIUserRegister.as_view()),
    path(r'', include('rest_auth.urls')),
    path(r'google/login/', include('rest_framework_social_oauth2.urls')),
]
