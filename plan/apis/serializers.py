from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import *

# Serializers are responsible to handle all the logic for the data 
# the viewset pass the data directly to it ( parse request, call the serializer.save() method, that create or update an instance then pass back the validateddata
# to the viewset that call the response)
# This is the body of the create mixin of a default post api
#
#   serializer = self.get_serializer(data=request.data)
#   serializer.is_valid(raise_exception=True)
#   self.perform_create(serializer) // this call the serializer that validates data and do all operations
#   headers = self.get_success_headers(serializer.data)
#   return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
# 
#
# Serializers transform the json data to data that can be handled by django
# It applies validation when receveing data 
# and when send back the response it reconvert the python complex object into json or some human readable datas
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
    customer = CustomerSerializer(required=True)

    class Meta: 
        model = Project
        fields = '__all__'
        
    def __init__(self, customer_serializer_included=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_serializer_included = customer_serializer_included
        if not customer_serializer_included: 
            self.fields.pop('customer')

    # This is call everytime some data are sent to the serializer (reading)
    def validate(self, attr):
        # check if customer exists here 
        if self.customer_serializer_included and not Customer.objects.filter(id = attr['customer']['id']).exists():
            raise ValidationError({ 'customer': 'customer needs to exists'})

        return attr

    # Here is handled the logic to create a project
    # I extend the create method of serializer because it is not able to handle nested relations
    # Nested object needs to be removed
    def create(self, validated_data):
        # 1 possible method: get a data that can be handled by django ( a query return an object that can be handled)
        # validate_data['customer'] = Customer.objects.get(id = validated_data['customer']['id'])
        # 2 possible method: use the orm to attach the customer_id to the new instance
        # this is possible because the column is defined in the DB and this doesn't raise an error
        customer = validated_data.pop('customer')
        project = Project.objects.create(customer_id = customer['id'], **validated_data) 
        return project

    # First version of update
    def update(self, instance, validated_data):
        print("update")
        customer = validated_data.pop('customer')
        Project.objects.filter(id = validated_data['id']).update(customer_id = customer['id'], **validated_data)       
       
        return Project.objects.get(id = validated_data['id'])


    # Second version of update
    # def update(self, instance, validated_data):
    #     # Convert the python object to complex data object of the orm
    #     customer = Customer.objects.get(id = validated_data.pop('customer')['id'])
        
    #     project = super().update(instance, validated_data)
    #     project.customer = customer
    #     project.save()

    #     return project
            
# class FinancialActivitySerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#     purchase_activity = serializers.IntegerField()
#     billing_activity = serializers.IntegerField()

#     class Meta: 
#         model = FinancialActivity
#         fields = '__all__'

#     def validate(self, attr): 
        
#         if att['purchase_activity']:
#             if not PurchaseActivity.objects.filter(id = attr['purchase_activity']['id']).exists():
#                 raise({'purchaseActivity': 'Needs to exist'})

#         if att['billing_activity']:
#             if not BillingActivity.objects.filter(id = attr['billing_activity']['id']).exists():
#                 raise({'billingActivity': 'Needs to exist'})   

#         return attr

#     def create(self, validated_data):
#         return FinancialActivity.objects.create(**validated_data) 

#     def update(self, instance, validated_data): 
        
#         if validated_data['purchase_activity']:
#             purchase_activity = validated_data.pop('purchase_activity')
#         if validated_data['billing_activity']: 
#             billing_activity = validated_data.pop('billing_activity')

#         PurchaseActivity.objects.update(validated_data['id'])
        

class BillingActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 
    # financial_activity =  FinancialActivitySerializer(required=True)
    # this permitts to user this serializer for this field
    project = ProjectSerializer(required=True, customer_serializer_included = False)
    
    class Meta: 
        model = BillingActivity
        fields = '__all__'
        
    def validate(self, attr):
        # Check if project id exists
        if not Project.objects.filter(id = attr['project']['id']).exists(): 
            raise ValidationError({'project': 'Project needs to exists'})
        # Check if financial activity exists
        # if not FinancialActivity.objects.filter(id = attr['financial_activity']['ìd']).exists():
        #     raise ValidationError({'financial_activity': 'Financial activity needs to exists'})
        return attr

    def create(self, validated_data):
        # financial_activity = validated_data.pop('financial_activity')
        project_id = validated_data.pop('project')['id']
        billing_activity = BillingActivity.objects.create(project_id = project_id , **validated_data)

        # FinancialActivity.objects.create(financial_activity)
        # validated_data['financial_activity'] = financial_activity
        
        return billing_activity

    def update(self, instance, validated_data):
        validated_data.pop('project')
        BillingActivity.objects.filter(id = validated_data['id']).update(**validated_data)       
       
        return BillingActivity.objects.get(id = validated_data['id'])

class PurchaseActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 
    # financial_activity =  FinancialActivitySerializer(required=True)
    # this permitts to user this serializer for this field
    project = ProjectSerializer(required=True, customer_serializer_included = False)
    
    class Meta: 
        model = PurchaseActivity
        fields = '__all__'
        
    def validate(self, attr):
        # Check if project id exists
        if not Project.objects.filter(id = attr['project']['id']).exists(): 
            raise ValidationError({'project': 'Project needs to exists'})
        # Check if financial activity exists
        # if not FinancialActivity.objects.filter(id = attr['financial_activity']['ìd']).exists():
        #     raise ValidationError({'financial_activity': 'Financial activity needs to exists'})
        return attr

    def create(self, validated_data):
        # financial_activity = validated_data.pop('financial_activity')
        project_id = validated_data.pop('project')['id']
        purchase_activity = PurchaseActivity.objects.create(project_id = project_id , **validated_data)

        # FinancialActivity.objects.create(financial_activity)
        # validated_data['financial_activity'] = financial_activity
        
        return purchase_activity

    def update(self, instance, validated_data):
        validated_data.pop('project')
        PurchaseActivity.objects.filter(id = validated_data['id']).update(**validated_data)       
       
        return PurchaseActivity.objects.get(id = validated_data['id'])


class SaleActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 
    # financial_activity =  FinancialActivitySerializer(required=True)
    # this permitts to user this serializer for this field
    project = ProjectSerializer(required=True, customer_serializer_included = False)
    
    class Meta: 
        model = SaleActivity
        fields = '__all__'
        
    def validate(self, attr):
        # Check if project id exists
        if not Project.objects.filter(id = attr['project']['id']).exists(): 
            raise ValidationError({'project': 'Project needs to exists'})
        # Check if financial activity exists
        # if not FinancialActivity.objects.filter(id = attr['financial_activity']['ìd']).exists():
        #     raise ValidationError({'financial_activity': 'Financial activity needs to exists'})
        return attr

    def create(self, validated_data):
        # financial_activity = validated_data.pop('financial_activity')
        project_id = validated_data.pop('project')['id']
        sale_activity = SaleActivity.objects.create(project_id = project_id , **validated_data)

        # FinancialActivity.objects.create(financial_activity)
        # validated_data['financial_activity'] = financial_activity
        
        return sale_activity

    def update(self, instance, validated_data):
        validated_data.pop('project')
        SaleActivity.objects.filter(id = validated_data['id']).update(**validated_data)       
       
        return SaleActivity.objects.get(id = validated_data['id'])


class WorkActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 
    project = ProjectSerializer(required=True, customer_serializer_included=False)

    class Meta: 
        model = WorkActivity
        fields = '__all__'

    def validate(self, att):   
        # Check if project id exists
        if not Project.objects.filter(id = attr['project']['id']).exists(): 
            raise ValidationError({'project': 'Project needs to exists'})

    # def create(self, validated_data):
    #     validated_data.po
   

    