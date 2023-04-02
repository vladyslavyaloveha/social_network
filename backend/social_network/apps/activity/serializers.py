from django.contrib.auth import get_user_model
from rest_framework import serializers
from social_network.apps.activity.models import UserActivity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        fields = (
            "username",
            "last_login",
        )

        read_only_fields = (
            "user_name",
            "last_login",
        )


class UserActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserActivity

        fields = (
            "pk",
            "url",
            "created_at",
            "user",
        )

        read_only_fields = (
            "pk",
            "url",
            "created_at",
            "last_active",
            "user",
        )
