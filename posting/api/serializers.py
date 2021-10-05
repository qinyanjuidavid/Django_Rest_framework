from rest_framework import serializers

from posting.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "pk",
            "user",
            'title',
            'content',
            'timestamp'
        ]
        read_only_fields = ["user", "pk"]

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                "The title has already been used.")
        return value
        # Converts to json and validates data past
