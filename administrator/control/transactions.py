# get beneficiary loan schedules
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.control.serializers import TransactionSerializer
from common.control.jwt_authent import JWTAuthentication
from core.models import Transaction


class TransactionAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        pay_plans = Transaction.objects.filter(user_id=pk)
        serializer = TransactionSerializer(pay_plans, many=True)
        return Response(serializer.data)


class AllTransactionAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pay_plans = Transaction.objects.all()
        serializer = TransactionSerializer(pay_plans, many=True)
        return Response(serializer.data)
