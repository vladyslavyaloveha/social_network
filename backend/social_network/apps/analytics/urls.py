from django.urls import include, path
from rest_framework import routers

from .views import AnalyticsViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"analytics", AnalyticsViewSet, basename="analytics")

urlpatterns = [
    path("", include(router.urls)),
]
