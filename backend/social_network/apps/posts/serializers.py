from rest_framework.serializers import (CurrentUserDefault, HiddenField,
                                        ModelSerializer)
from social_network.apps.posts.models import Like, Post


class PostSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            "pk",
            "description",
            "user",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "pk",
            "created_at",
            "updated_at",
        )


class PostLikeSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("pk",)


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "pk",
            "user",
            "post",
            "created_at",
        )
        read_only_fields = (
            "pk",
            "created_at",
        )
