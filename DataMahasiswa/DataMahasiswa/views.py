from .models import Data
from rest_framework import viewsets
from .serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):

    queryset = Data.objects.all()
    serializer_class = DataSerializer