from rest_framework import routers
from .api import FeedbackViewSet

router = routers.DefaultRouter()
router.register('feedback', FeedbackViewSet, 'feedback')

urlpatterns = router.urls
