from rest_framework.routers import SimpleRouter
from .api.views import BookingViewSet

router = SimpleRouter()

router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = router.urls
