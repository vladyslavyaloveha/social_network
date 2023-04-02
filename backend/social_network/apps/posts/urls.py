from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
]
