from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mainapp.models import FoodCategory
from mainapp.serializers import FoodListSerializer


class FoodModelViewSet(ModelViewSet):
    queryset = FoodCategory.objects.exclude(food__isnull=True)
    serializer_class = FoodListSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return FoodListSerializer
        raise Http404


