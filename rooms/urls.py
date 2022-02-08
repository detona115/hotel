from django.urls import path
from rest_framework.routers import SimpleRouter
from .api.views import RoomViewSet

router = SimpleRouter()

router.register('rooms', RoomViewSet, basename='rooms')

urlpatterns = router.urls