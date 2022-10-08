from rest_framework import serializers
from core.models import LoanSchedule, User, Transaction


class LoanPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanSchedule
        fields = '__all__'


class LoanBeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'