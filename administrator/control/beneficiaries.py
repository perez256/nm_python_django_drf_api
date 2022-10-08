import datetime as dt
import decimal
from rest_framework import generics, mixins, exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.control.serializers import LoanScheduleSerializer
from common.control.jwt_authent import JWTAuthentication
from common.control.serializers import BeneficiarySerializer

from core.models import User, LoanSchedule


class BeneficiaryAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.filter(is_beneficiary=True)
    serializer_class = BeneficiarySerializer

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


class RegisterBeneficiaryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, incoming):
        data = incoming.data
        # if data['password'] != data['password_confirm']:
        #     raise exceptions.AuthenticationFailed('Passwords do not match')
        serializer = BeneficiarySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# get beneficiary loan schedules
class BeneficiaryPlanAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        pay_plans = LoanSchedule.objects.filter(user_id=pk)
        serializer = LoanScheduleSerializer(pay_plans, many=True)
        return Response(serializer.data)


# create payment plan pending
class CreatePlanAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, incoming, pk=None):
        if pk:
            # set the fields
            p = 0

            car_amount = incoming.data['car_amount']
            backup_amount = incoming.data['backup_amount']
            end_date = incoming.data['end_date']
            start_date = incoming.data['start_date']
            amount_per_week = incoming.data['amount_per_week']
            no_years = incoming.data['no_years']

            # set the date calucation variables
            datem = dt.datetime.strptime(end_date, "%Y-%m-%d")

            year1 = dt.datetime.date(datem).year
            month1 = dt.datetime.date(datem).month
            day1 = dt.datetime.date(datem).day
            print('perez compute date', int(year1), int(month1), int(day1))

            datex = dt.datetime.strptime(start_date, "%Y-%m-%d")
            year2 = dt.datetime.date(datex).year
            month2 = dt.datetime.date(datex).month
            day2 = dt.datetime.date(datex).day

            xending = dt.date(int(year1), int(month1), int(day1))
            xstarting = dt.date(int(year2), int(month2), int(day2))

            auto_weeks = abs(xending - xstarting).days  # pending calculation
            print(auto_weeks // 7)
            automatic_weeks = int(auto_weeks // 7)
            interest = 0
            rate = 0.3
            count_week = 0

            loan_balancex = car_amount

            # update the loan

            update_user_loan = User.objects.filter(id=pk).update(
                status='Incomplete',
                car_amount=car_amount,
                backup_amount=backup_amount,
                loan_balance=loan_balancex,
                amount_per_week=amount_per_week,
                no_weeks=automatic_weeks,
                no_years=no_years,
                start_date=start_date,
                end_date=end_date,
                interest=interest
            )
            expected_balance = car_amount

            startingAt = dt.datetime.strptime(start_date, "%Y-%m-%d")
            loan = User.objects.get(id=pk)

            while int(car_amount) > p:
                p += int(amount_per_week)
                install_balance = decimal.Decimal(amount_per_week)
                startingAt += dt.timedelta(7)
                balance_remaining = int(loan.loan_balance) - int(amount_per_week)
                User.objects.filter(id=pk).update(
                    cal_amount_remaining=balance_remaining
                )
                # generate plans
                LoanSchedule.objects.create(
                    user=loan,
                    start_date=startingAt.strftime('%Y-%m-%d'),
                    paid_on=startingAt.strftime('%Y-%m-%d'),
                    expected_install_amt=decimal.Decimal(amount_per_week),
                    amount_paid=0.00,
                    balance=decimal.Decimal(amount_per_week),
                    interest_rate=0.00,
                    late_pay_charge=0.00,
                    status='Not Paid'
                )
            count_schedule = LoanSchedule.objects.filter(user_id=loan.id).count()
            print('installment count', count_schedule)

            User.objects.filter(id=pk).update(
                no_weeks=int(count_schedule),
            )

            return Response({"success": "Payment plan has been generated successfully"}, status=status.HTTP_201_CREATED)
