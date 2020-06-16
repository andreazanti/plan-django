from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import *

# Serializers are responsible to handle all the logic for the data ( it communicates directly with FE)
class CustomerSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Customer
        fields = '__all__'

    # def validate(self, attrs):
    #     print(attrs)
    #     raise ValidationError('fdsfdas')
    #     return attrs

    # def create(self, validated_data):
    #     pass

    # def update(self, instance, validated_data):
    #     pass
    

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 
    customer =  CustomerSerializer(required=True)
    class Meta: 
        model = Project
        fields = '__all__'
        
    # This is call everytime some data are sent to the serializer (reading)
    def validate(self, attr):
        # check if customer exists here 
        if not Customer.objects.filter(id = attr['customer']['id']).exists():
            raise ValidationError({ 'customer': 'customer needs to exists'})

        return attr

    # Here is handled the logic to create a project
    # I extend the create method of serializer because it is not able to handle nested relations
    # Nested object needs to be removed
    def create(self, validated_data):
        print(validated_data)
        # 1 possible method: get a data that can be handled by django ( a query return an object that can be handled)
        # validate_data['customer'] = Customer.objects.get(id = validated_data['customer']['id'])
        # 2 possible method: use the orm to attach the customer_id to the new instance
        # this is possible because the column is defined in the DB and this doesn't raise an error
        customer = validated_data.pop('customer')
        project = Project.objects.create(customer_id = customer['id'], **validated_data) 
        return project

    # First version of update
    # def update(self, instance, validated_data):
    #     customer = validated_data.pop('customer')
    #     updated = Project.objects.filter(id = validated_data['id']).update(customer_id = customer['id'], **validated_data) 
    #     if(updated == 0) : 
    #         raise ValidationError('Some errors during update')
        
    #     validated_data['customer'] = customer
    #     return Project.objects.get(id = validated_data['id'])


    # Second version of update
    def update(self, instance, validated_data):
        # Convert the python object to complex data object of the orm
        customer = Customer.objects.get(id = validated_data.pop('customer')['id'])
        
        project = super().update(instance, validated_data)
        project.customer = customer
        project.save()

        return project
            

class BillingActivitySerializer(serializers.ModelSerializer):
    pass