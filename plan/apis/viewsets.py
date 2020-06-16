from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from plan.models import *
from plan.apis.serializers import *


class CustomerViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # Define my custom endpoint
    # If detail is true indicate that the current action is configured for a list or detail views
    # This action is binded to /customers/count
    # @action(detail=False, methods=['get'])
    # def count(self, *args, **kwargs):
    #    count = Customer.objects.all().count()
    #    return Response({
    #        'count': count
    #    })

    # This action is binded to /customers/{detail_id}/extended because there is detail true
    # @action(detail=True, methods=['get'])
    # def extended(self, *args, **kwargs):
    #    instance = self.get_object()
    #    serializer = self.get_serializer(instance)
    #    return Response({
    #        'customer': serializer.data,
    #        'extended': True
    #    })



class ProjectViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
