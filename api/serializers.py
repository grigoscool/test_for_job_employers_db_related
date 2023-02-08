from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
