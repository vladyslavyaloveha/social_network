from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiParameter, OpenApiResponse,
                                   extend_schema, extend_schema_view)
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from social_network.apps.activity.models import UserActivity
from social_network.apps.activity.serializers import UserActivitySerializer
from social_network.apps.common.serializers import ErrorSerializer


@extend_schema_view(
    retrieve=extend_schema(
        summary="Inspect activity",
        responses={
            200: OpenApiResponse(UserActivitySerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    list=extend_schema(
        summary="List activities",
        parameters=[
            OpenApiParameter(
                "user",
                OpenApiTypes.INT,
                OpenApiParameter.QUERY,
                required=True,
                description="A pk identifying a user.",
            ),
        ],
        responses={
            200: OpenApiResponse(UserActivitySerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
)
class UserActivityViewSet(ReadOnlyModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )
    filterset_fields = ["user"]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ("last_active",)
    ordering = ("-last_active",)
