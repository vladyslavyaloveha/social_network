from django.db.models import Count
from django.db.models.functions import TruncDay
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiExample, OpenApiParameter,
                                   OpenApiResponse, extend_schema,
                                   extend_schema_view)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from social_network.apps.analytics.serializers import LikesQuerySerializer
from social_network.apps.common.serializers import ErrorSerializer
from social_network.apps.posts.models import Like


@extend_schema_view(
    likes=extend_schema(
        summary="Get likes analytics",
        parameters=[
            OpenApiParameter(
                "start_date",
                OpenApiTypes.DATE,
                OpenApiParameter.QUERY,
                required=True,
                description="Start date",
                examples=[
                    OpenApiExample("start_date", value="2023-04-01"),
                ],
            ),
            OpenApiParameter(
                "end_date",
                OpenApiTypes.DATE,
                OpenApiParameter.QUERY,
                required=True,
                description="End date",
                examples=[
                    OpenApiExample("end_date", value="2023-05-01"),
                ],
            ),
        ],
        responses={
            200: OpenApiResponse(
                OpenApiTypes.STR,
                description="Success",
                examples=[
                    OpenApiExample(
                        "likes", value={"date": "2023-04-03T00:00:00Z", "likes": 1}
                    ),
                ],
            ),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
)
class AnalyticsViewSet(GenericViewSet):
    serializer_class = None
    filterset_fields = ["start_date", "end_date"]

    @action(methods=["get"], detail=False)
    def likes(self, request):
        serializer = LikesQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        start_date, end_date = (
            serializer.data["start_date"],
            serializer.data["end_date"],
        )
        result = self._get_likes(start_date, end_date)
        return Response(data=result, status=status.HTTP_200_OK)

    @staticmethod
    def _get_likes(start_date: str, end_date: str) -> int:
        likes = (
            Like.objects.filter(created_at__range=[start_date, end_date])
            .annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(likes=Count("id"))
            .order_by("-likes")
        )
        return likes
