from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiExample, OpenApiParameter,
                                   OpenApiResponse, extend_schema,
                                   extend_schema_view)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from social_network.apps.common.serializers import ErrorSerializer
from social_network.apps.posts.models import Post
from social_network.apps.posts.permissions import IsPostOwnerOrReadOnly
from social_network.apps.posts.serializers import (PostLikeSerializer,
                                                   PostSerializer)


@extend_schema_view(
    create=extend_schema(
        summary="Create a new post",
        responses={
            201: OpenApiResponse(PostSerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    retrieve=extend_schema(
        summary="Inspect a post",
        responses={
            200: OpenApiResponse(PostSerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    list=extend_schema(
        summary="List posts",
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
            200: OpenApiResponse(PostSerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    update=extend_schema(
        summary="Update a post",
        responses={
            200: OpenApiResponse(PostSerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    partial_update=extend_schema(
        summary="Partial update a post",
        responses={
            200: OpenApiResponse(PostSerializer, description="Success"),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    destroy=extend_schema(
        summary="Remove a post",
        responses={
            204: None,
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
    like=extend_schema(
        summary="Like a post",
        responses={
            200: OpenApiResponse(
                OpenApiTypes.STR,
                description="Success",
                examples=[
                    OpenApiExample("like", value={"is_liked": True}),
                    OpenApiExample("dislike", value={"is_liked": False}),
                ],
            ),
            400: OpenApiResponse(ErrorSerializer, description="Invalid request"),
            404: OpenApiResponse(ErrorSerializer, description="Not found"),
            500: OpenApiResponse(ErrorSerializer, description="Server error"),
        },
    ),
)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsPostOwnerOrReadOnly,
    )

    def get_serializer_class(self):
        match self.action:
            case "like":
                return PostLikeSerializer
            case _:
                return PostSerializer

    @action(methods=["post"], detail=True, permission_classes=(IsAuthenticated,))
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if post.likes.filter(pk=user.pk).exists():
            post.likes.remove(user)
            is_liked = False
        else:
            post.likes.add(user)
            is_liked = True
        return Response({"is_liked": is_liked}, status=status.HTTP_200_OK)
