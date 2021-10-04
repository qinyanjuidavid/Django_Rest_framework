from rest_framework import serializers

from posting.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = "BlogPost"
        fields = [
            "pk",
            "user",
            'title',
            'content',
            'timestamp'
        ]
# Converts to json and validates data past
