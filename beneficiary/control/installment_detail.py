from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from beneficiary.control.serializers import LoanPlanSerializer
from common.control.jwt_authent import JWTAuthentication
from core.models import LoanSchedule


class InstallDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, incoming, pk=None):
        if pk and LoanSchedule:
            print(str(pk))
            schedule = LoanSchedule.objects.get(id=pk)
            serializer = LoanPlanSerializer(schedule, many=False)
            return Response(serializer.data)
        return exceptions.APIException('Failed to get ID')

