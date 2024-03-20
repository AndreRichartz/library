from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet


from library.models import Category
from library.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
