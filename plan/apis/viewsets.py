from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from plan.models import *
from plan.apis.serializers import *


# A view set is responsible to handle all the operations for the data
# It defines the query set to which do operations
# and a serializer class that takes the request,
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

class BillingActivityViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = BillingActivity.objects.all()
    serializer_class = BillingActivitySerializer


class PurchaseActivityViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = PurchaseActivity.objects.all()
    serializer_class = PurchaseActivitySerializer

class SaleActivityViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = SaleActivity.objects.all()
    serializer_class = SaleActivitySerializer

class WorkActivityViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = WorkActivity.objects.all()
    serializer_class = WorkActivitySerializer

# class FinancialActivityViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):

#     queryset = FinancialActivity.objects.all()
#     serializer_class = FinancialActivitySerializer
    
