from django.contrib import admin
from plan.models import *
# from plan.forms import ListForm
from django.contrib.admin.views.main import ChangeList

#TODO: create custom admin class that extends django admin class
admin.site.site_header = 'Plan - fuori città'
admin.site.site_title = 'Plan - fuori città'
admin.site.register(PurchaseActivity)
admin.site.register(WorkActivity)
admin.site.register(Customer)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # It controls which fields are shown in the list page
    list_display = ('customer','name', 'status')
    # It controls which fields are editable
    list_editable = ('customer','name', 'status')
    
    list_display_links = None    

    # This method can be used to override the 
    # default class for the list
    def get_changelist(request, **kwargs): 
        # return myClass
        return ChangeList

    def get_changelist_form(self, request, **kwargs):
        pass 

    def get_changelist_formset(self, request, **kwargs):
        pass
    
admin.site.register(BillingActivity)
admin.site.register(FinancialActivity)
admin.site.register(WorkLogActivity)