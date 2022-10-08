import time
from random import randrange

from django.core.management import BaseCommand
from faker import Faker

from core.models import CarLoan, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        k = 0
        for _ in range(5):
            k += 1
            user = User.objects.get(pk=k)
            CarLoan.objects.create(
                user=user,
                reg_number=faker.last_name(),
                chassis=faker.first_name(),
                car_image=faker.image_url(),
                car_amount=randrange(10, 10000),
                status='Incomplete'
            )
