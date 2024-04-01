from rest_framework import serializers


class SimpleBookSirializer(serializers.Serializer):
    title = serializers.CharField()
    year = serializers.IntegerField()
