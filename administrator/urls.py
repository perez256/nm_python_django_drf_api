from django.urls import path, include

from administrator.control.beneficiaries import BeneficiaryAPIView, RegisterBeneficiaryAPIView, CreatePlanAPIView, \
    BeneficiaryPlanAPIView
from administrator.control.staff import StaffAPIView
from administrator.control.transactions import TransactionAPIView, AllTransactionAPIView

urlpatterns = [
    path('', include('common.urls')),
    #     Create Loan
    # crud Staff | # List| update| Detail | delete
    path('staff', StaffAPIView.as_view(), name='staffs'),
    path('staff/<str:pk>', StaffAPIView.as_view(), name='staff'),
    # crud beneficiaries | # List| update| Detail | delete
    path('beneficiaries', BeneficiaryAPIView.as_view(), name='beneficiaries'),
    path('create_beneficiary', RegisterBeneficiaryAPIView.as_view(), name='create_beneficiary'),
    path('beneficiaries/<str:pk>', BeneficiaryAPIView.as_view(), name='beneficiary'),
    path('payment_plans/<str:pk>', BeneficiaryPlanAPIView.as_view(), name='payment_plans'),
    path('create_plan/<str:pk>', CreatePlanAPIView.as_view(), name='create_plan'),
    #     transactions
    path('transactions/<str:pk>', TransactionAPIView.as_view(), name='payment_plans'),
    path('all_transactions/', AllTransactionAPIView.as_view(), name='payment_plans'),
]
