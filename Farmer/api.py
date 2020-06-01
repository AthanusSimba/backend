from .models import Farmer
from rest_framework import viewsets, permissions
from .serializers import FarmerSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    permission_classes = [
        # permissions.IsAuthenticated
        permissions.AllowAny
    ]
    serializer_class = FarmerSerializer

    '''def get_querySet(self):
        # return self.request.user.farmer.all()
        return self.queryset'''

    '''def perform_create(self, serializer):
        serializer.save(owner=self.request.user)'''