from rest_framework import serializers


class LikesQuerySerializer(serializers.Serializer):  # noqa
    start_date = serializers.DateField(format="%Y-%m-%d")
    end_date = serializers.DateField(format="%Y-%m-%d")
