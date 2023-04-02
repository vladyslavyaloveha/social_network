from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):  # noqa
    detail = serializers.CharField()
