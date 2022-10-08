from django.urls import path, include

from beneficiary.control.get_pay_plans import SchedulePlansAPIView, TransactionAPIView
from beneficiary.control.installment_detail import InstallDetailAPIView
from beneficiary.control.loan import LoanBeneficiaryAPIView
from beneficiary.control.receipts import ReceiptDetailAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('pay_plan', SchedulePlansAPIView.as_view(), name='pay_plan'),
    path('transactions', TransactionAPIView.as_view(), name='transactions'),
    path('transactions/<str:pk>', InstallDetailAPIView.as_view(), name='transactions'),
    path('receipt/<str:pk>', ReceiptDetailAPIView.as_view(), name='transactions'),
]
