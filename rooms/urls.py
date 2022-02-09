from rest_framework.routers import SimpleRouter

from .api import RoomViewSet

router = SimpleRouter()

router.register('rooms', RoomViewSet, basename='rooms')

urlpatterns = router.urls
