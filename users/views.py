from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer, PublicUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.pk == self.get_object().pk:
            return UserSerializer
        return PublicUserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



