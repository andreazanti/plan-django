from rest_framework import routers
from plan.apis.viewsets import *

router = routers.SimpleRouter()

router.register('customers', CustomerViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = router.urls;