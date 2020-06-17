from rest_framework import routers
from plan.apis.viewsets import *

router = routers.SimpleRouter()

router.register('customers', CustomerViewSet)
router.register('projects', ProjectViewSet)
router.register('billing-activities', BillingActivityViewSet)
router.register('purchase-activities', PurchaseActivityViewSet)
router.register('sale-activities', SaleActivityViewSet)
router.register('work-activities', WorkActivityViewSet)
# router.register('financial-activities', FinancialActivityViewSet)

urlpatterns = router.urls
