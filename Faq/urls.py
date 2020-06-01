from rest_framework import routers
from .api import FaqsViewSet

router = routers.DefaultRouter()
router.register('faqs', FaqsViewSet, 'faqs')

urlpatterns = router.urls
