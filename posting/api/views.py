from django.shortcuts import render
from posting.models import BlogPost
from posting.api.serializers import BlogPostSerializer
from rest_framework import generics


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = BlogPostSerializer
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return BlogPost.objects.get(pk=pk)
# RetriveAPIView
# RetrieveUpdateDestoyAPIView
# RetriveDestoyAPIView
