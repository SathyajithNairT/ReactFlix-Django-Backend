from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import ShowDataModel
from .views import ShowDataViewSet, get_data, get_unique_grouping, get_all_data

router = DefaultRouter()
router.register('add-show-data', ShowDataViewSet, basename= 'add-show-data')

@api_view(['GET'])
def api_root(request, format = None):
    default_grouping = 'Animation'

    return Response({
        'Add Show Data': reverse('add-show-data-list', request= request, format= format),
        'Get all Data': reverse('all-data', request= request, format= format),
        'Get data by grouping': reverse('get-data', kwargs={'grouping': default_grouping}, request= request, format= format),
        'Grouping': reverse('grouping', request= request, format= format)
    })

urlpatterns = [
    path('', api_root, name = 'api_root'),
    path('get-data/<grouping>/', get_data, name = 'get-data'),
    path('', include(router.urls)),
    path('grouping/', get_unique_grouping, name= 'grouping'),
    path('all-data/', get_all_data, name= 'all-data')
]