from rest_framework import routers
from users.apis.viewsets import *

router = routers.SimpleRouter()

router.register('users', UserViewSet)

urlpatterns = router.urls
