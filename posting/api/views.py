from django.shortcuts import render
from rest_framework import generics
from posting.models import BlogPost


class BlogPostRudView(generics.RetrieveUpdateDestoyAPIView):
    loojup_field = "pk"
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return BlogPost.objects.get(pk=pk)
