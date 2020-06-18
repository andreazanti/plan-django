from django.contrib import admin
from .models import WorkLogActivity,PurchaseActivity, WorkActivity, BillingActivity, SaleActivity,FinancialActivity,  Project, Customer

admin.site.register(PurchaseActivity)
admin.site.register(WorkActivity)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(SaleActivity)
admin.site.register(BillingActivity)
admin.site.register(FinancialActivity)
admin.site.register(WorkLogActivity)