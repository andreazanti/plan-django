from enum import Enum
import django
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from commons.models import CustomBaseModel
from django.db import models
from users.models import User

STATUS = (
    ('new','new'),
    ('open','open'),
    ('closed','closed')
)

WORK_ACTIVITY_TYPE = (
    ('web','web'),
    ('mobile','mobile')
)


class Customer(CustomBaseModel): 
    contact = models.CharField(max_length= 2048)
    email = models.EmailField(max_length= 2048)
class Project(CustomBaseModel):
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=128)
    status = models.CharField(choices=STATUS, max_length = 2048)

    def __str__(self):
        return self.name
    
class SaleActivity(CustomBaseModel):
    desc = models.CharField(max_length= 2048)
    days = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(choices=STATUS, max_length= 2048)
    project = models.ForeignKey(Project, on_delete= models.CASCADE)

class WorkActivity(CustomBaseModel):
    desc = models.CharField(null=True, blank=True, max_length= 2048)
    days = models.IntegerField(validators=[MinValueValidator(0)])
    type = models.CharField(choices=WORK_ACTIVITY_TYPE, max_length= 2048)
    status = models.CharField(choices=STATUS, max_length= 2048)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.desc

class FinancialActivity(CustomBaseModel):
    invoice_number = models.CharField(null= True, blank = True, max_length= 2048)
    invoice_date = models.DateTimeField(null= True, blank= True, max_length= 2048)
    incoming = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
    charge = models.IntegerField(default= 0, validators=[MaxValueValidator(0)])

class PurchaseActivity(CustomBaseModel):
    desc = models.CharField(max_length= 2048)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # financial_activity = models.OneToOneField(FinancialActivity, on_delete=models.CASCADE)

class BillingActivity(CustomBaseModel):
    desc = models.CharField(max_length= 2048)
    days = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # financial_activity = models.OneToOneField(FinancialActivity, on_delete=models.CASCADE)

class WorkLogActivity(CustomBaseModel):
    desc = models.CharField(max_length=128)
    day = models.DateField(default= django.utils.timezone.now)
    hours = models.FloatField(validators= [MinValueValidator(0)])
    work_activity = models.ForeignKey(WorkActivity, on_delete= models.SET_NULL, null = True)
    #TODO: put user ref here