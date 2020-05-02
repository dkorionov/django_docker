from django.urls import path, include
from video_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'video', views.VideoViewSet, basename='video'),

urlpatterns = router.urls
