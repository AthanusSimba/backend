from .models import Faqs
from rest_framework import viewsets, permissions
from .serializers import FaqsSerializer


class FaqsViewSet(viewsets.ModelViewSet):
    queryset = Faqs.objects.all()
    permission_classes = [
        # permissions.IsAuthenticated
        permissions.AllowAny
    ]
    serializer_class = FaqsSerializer

    '''def get_querySet(self):
        # return self.request.user.farmer.all()
        return self.queryset'''

    '''def perform_create(self, serializer):
        serializer.save(owner=self.request.user)'''
