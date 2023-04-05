from rest_framework import serializers
from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ('id', 'short_code', 'long_url', 'title', 'created_at', 'updated_at')
