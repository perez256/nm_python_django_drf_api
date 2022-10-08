from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from beneficiary.control.serializers import LoanPlanSerializer, TransactionSerializer
from common.control.jwt_authent import JWTAuthentication
from core.models import LoanSchedule, Transaction


class SchedulePlansAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, incoming):
        user = incoming.user
        schedule = LoanSchedule.objects.filter(user_id=user.id).filter(status='Not Paid')
        serializer = LoanPlanSerializer(schedule, many=True)
        return Response(serializer.data)


class TransactionAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, incoming):
        user = incoming.user
        transaction = Transaction.objects.filter(user_id=user.id).filter(status='Paid')
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
