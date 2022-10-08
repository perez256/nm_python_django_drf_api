from rest_framework import generics, mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from common.control.jwt_authent import JWTAuthentication
from common.control.serializers import StaffSerializer
from core.models import User


class StaffAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.filter(is_superuser=True)
    serializer_class = StaffSerializer

    def get(self, incoming, pk=None):
        if pk:
            return self.retrieve(incoming, pk=pk)
        return self.list(incoming)

    def post(self, incoming):
        if incoming.user.is_superuser:
            return self.create(incoming)
        raise exceptions.AuthenticationFailed('You are unauthorized')

    def put(self, incoming, pk=None):
        return self.partial_update(incoming, pk)

    def delete(self, incoming, pk=None):
        return self.destroy(incoming, pk)
