from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from Blog.models import Categoria , Post

from .serializers import (CategoriaSerializer , PostSerializer)

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


