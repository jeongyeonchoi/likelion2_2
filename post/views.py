from django.shortcuts import render
from post.models import Post
from post.serializer import PostSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse
from .pagination import MyPagination

class MyPagination(PageNumberPagination):
    page_size = 5

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = MyPagination

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")