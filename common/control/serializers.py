from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'mtn_number', 'airtel_number', 'is_blocked',
                  'country', 'is_beneficiary']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'mtn_number',
                  'airtel_number',
                  'is_superuser', 'is_beneficiary', 'nin_number', 'country', 'reg_number', 'chassis', 'model', 'brand',
                  'year', 'color', 'gaurantor1_name', 'gaurantor1_phone', 'gaurantor1_email', 'gaurantor2_name',
                  'gaurantor2_phone', 'gaurantor2_email', 'car_amount', 'loan_balance', 'amount_per_week', 'no_weeks',
                  'no_years', 'start_date', 'end_date']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        # def create(self, validated_data):
        #     instance = self.Meta.model(**validated_data)
        #     instance.is_superuser = False
        #     instance.is_beneficiary = True
        #     instance.is_staff = False
        #     instance.is_active = True
        #     instance.save()
        #


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'mtn_number', 'airtel_number',
                  'is_superuser', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.is_superuser = True
            instance.is_staff = True
            instance.is_active = True
            instance.save()
            return instance
