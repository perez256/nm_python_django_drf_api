from rest_framework import serializers
from common.control.serializers import UserSerializer
from core.models import LoanSchedule, Transaction


class LoanScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = LoanSchedule
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Transaction
        fields = '__all__'
