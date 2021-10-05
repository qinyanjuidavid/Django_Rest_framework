from django.shortcuts import render
from posting.models import BlogPost
from posting.api.serializers import BlogPostSerializer
from rest_framework import generics, mixins
from django.db.models import Q
from posting.api.permissions import IsOwnerOrReadOnly


class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BlogPostSerializer
    # permission_classes = []

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query),
                           Q(content__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    def get_serializer_content(self, *args, **kwargs):
        return {"request": self.request}

        # def get_object(self):
        #     pk = self.kwargs.get('pk')
        #     return BlogPost.objects.get(pk=pk)
        # RetriveAPIView
        # RetrieveUpdateDestoyAPIView
        # RetriveDestoyAPIView
        # ListAPIView
        # CreateAPIView
        #
