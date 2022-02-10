from rest_framework.routers import SimpleRouter

from .api import BookingViewSet

router = SimpleRouter()

router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = router.urls
