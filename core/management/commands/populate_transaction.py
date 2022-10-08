from django.core.management import BaseCommand
from faker import Faker

from core.models import User, Transaction, LoanSchedule


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        k = 0
        for _ in range(2):
            k += 1
            user = User.objects.get(pk=k)
            loan_schedule = LoanSchedule.objects.get(id=450)
            Transaction.objects.create(
                user=user,
                loan_schedule_id=loan_schedule,
                amount_paid=150000,
                balance=0,
                expected_amount=300000,
                payment_method='MTN',
                transaction_id='XFDT50' + str(k),
                status='PAID'
            )
