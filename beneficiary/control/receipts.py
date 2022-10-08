from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from beneficiary.control.serializers import TransactionSerializer
from common.control.jwt_authent import JWTAuthentication
from core.models import Transaction


class ReceiptDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, incoming, pk=None):
        if pk:
            transaction = Transaction.objects.get(id=pk)
            serializer = TransactionSerializer(transaction, many=False)
            return Response(serializer.data)
        return exceptions.APIException('Something went wrong')
