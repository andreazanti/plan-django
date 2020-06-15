from enum import Enum

import django
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.db import models

STATUS = (
    ('web','web'),
    ('mobile','mobile')
)

WORK_ACTIVITY_TYPE = (
    ('new','new'),
    ('open','open'),
    ('closed','closed')
)

class CustomBaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    notes = models.CharField(null = True, blank = True, max_length = 2048)
    # This set the class as abstract class and does not create a 1 to 1 relation when extending the class
    class Meta:
        abstract = True

class Customer(CustomBaseModel):
    contact = models.CharField(max_length= 2048)
    email = models.CharField(validators = [EmailValidator], max_length= 2048)

class Project(CustomBaseModel):
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=2048)

class SaleActivity(CustomBaseModel):
    desc = models.CharField(max_length= 2048)
    days = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(choices=STATUS, max_length= 2048)
    project = models.ForeignKey(Project, on_delete= models.CASCADE)

class WorkActivity(CustomBaseModel):
    desc = models.CharField(null=True, blank=True, max_length= 2048)
    days = models.IntegerField(validators=[MinValueValidator(0)])
    type = models.CharField(choices=WORK_ACTIVITY_TYPE, max_length= 2048)
    status = models.CharField(choices=STATUS, max_length= 2048)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #TODO: add user ref

class FinancialActivity(CustomBaseModel):
    invoice_number = models.CharField(null= True, blank = True, max_length= 2048)
    invoice_date = models.DateTimeField(null= True, blank= True, max_length= 2048)
    incoming = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
    charge = models.IntegerField(default= 0, validators=[MaxValueValidator(0)])

class PurchaseActivity(CustomBaseModel):
    desc = models.CharField(max_length= 2048)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    financial_activity = models.OneToOneField(FinancialActivity, on_delete=models.CASCADE)

class BillingActivity(CustomBaseModel):
    desc = models.CharField(max_length= 2048)
    days = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    financial_activity = models.OneToOneField(FinancialActivity, on_delete=models.CASCADE)

class WorkLogActivity(CustomBaseModel):
    desc = models.CharField(max_length=2048)
    day = models.DateField(default= django.utils.timezone.now)
    hours = models.FloatField(validators= [MinValueValidator(0)])
    work_activity = models.ForeignKey(WorkActivity, on_delete= models.SET_NULL, null = True)
    #TODO: put user ref here
