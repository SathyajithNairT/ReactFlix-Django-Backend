from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ShowDataModel
from .serializers import ShowDataSerializer

# Create your views here.


class ShowDataViewSet(viewsets.ModelViewSet):
    queryset = ShowDataModel.objects.all()
    serializer_class = ShowDataSerializer


@api_view(['GET'])
def get_data(request, grouping):
    grouped_data = ShowDataModel.objects.filter(grouping = grouping)

    serializer = ShowDataSerializer(grouped_data, many= True)

    return Response(serializer.data)


@api_view(['GET'])
def get_unique_grouping(request):
    unique_groupings = ShowDataModel.objects.values_list('grouping', flat= True).distinct()
    return Response(unique_groupings)


@api_view(['GET'])
def get_all_data(request):
    all_data = ShowDataModel.objects.all()

    serializer = ShowDataSerializer(all_data, many= True)

    return Response(serializer.data)