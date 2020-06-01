from .models import Feedback
from rest_framework import viewsets, permissions
from .serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    permission_classes = [
        # permissions.IsAuthenticated
        permissions.AllowAny
    ]
    serializer_class = FeedbackSerializer

    '''def get_querySet(self):
        # return self.request.user.farmer.all()
        return self.queryset'''

    '''def perform_create(self, serializer):
        serializer.save(owner=self.request.user)'''