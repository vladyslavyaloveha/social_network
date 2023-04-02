from django.urls import include, path
from rest_framework import routers

from .views import UserActivityViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"activity", UserActivityViewSet, basename="activity")

urlpatterns = [
    path("", include(router.urls)),
]
