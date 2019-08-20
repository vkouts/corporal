from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api.api import PictureViewSet, BackColorViewSet


router = DefaultRouter()
router.register('colors', BackColorViewSet)
router.register('pictures', PictureViewSet)

urlpatterns = [
	path('', include(router.urls)),
]