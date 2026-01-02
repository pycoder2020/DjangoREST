from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, StatsView

router = DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', StatsView.as_view(), name='stats'),
]
