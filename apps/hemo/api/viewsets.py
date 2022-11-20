from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import HemoSerializer

from ..models import Hemo


class HemoViewset(ModelViewSet):

    serializer_class = HemoSerializer
    # permission_classes = [IsAuthenticated]
    filterset_fields = ["is_active", "last_login"]
    queryset = Hemo.objects.all()
