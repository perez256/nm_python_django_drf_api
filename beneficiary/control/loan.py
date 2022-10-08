from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from beneficiary.control.serializers import LoanBeneficiarySerializer
from common.control.jwt_authent import JWTAuthentication


class LoanBeneficiaryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, incoming):
        # user = incoming.user
        # loan = CarLoan.objects.get(user_id=user.id)
        # serializer = LoanBeneficiarySerializer(loan, many=False)
        # return Response(serializer.data)
        pass
