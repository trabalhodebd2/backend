from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer, UserProfileSerializer

from .permissions import ChangePasswordPermission
from rest_framework.permissions import IsAuthenticated

from apps.custom_auth.models import User


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['is_active', 'last_login']
    queryset = User.objects.filter(is_active=True)

    # TODO: TESTAR MELHOR ESSA ACTION
    @action(detail=True, methods=['PATCH'], permission_classes=[IsAuthenticated, ChangePasswordPermission])
    def change_password(self, request, pk=None):

        user = self.get_object()
        new_password = request.data.get('password', None)

        if new_password is not None:
            user.set_password(new_password)
            user.save()

        return Response({'status': 'password set'})

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated], serializer_class=UserProfileSerializer)
    def profile(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
