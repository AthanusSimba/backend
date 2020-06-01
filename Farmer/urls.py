from rest_framework import routers
from .api import FarmerViewSet

router = routers.DefaultRouter()
router.register('farmer', FarmerViewSet, 'farmer')

urlpatterns = router.urls
