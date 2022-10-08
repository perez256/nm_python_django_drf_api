from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_beneficiary = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = True
        user.is_beneficiary = False
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_beneficiary = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    nin_number = models.CharField(max_length=200, blank=True, null=True)
    mtn_number = models.CharField(max_length=200, blank=True, null=True)
    airtel_number = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    reg_number = models.CharField(max_length=200, blank=True, null=True)
    chassis = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True, default=0)
    color = models.CharField(max_length=200, blank=True, null=True)

    status = models.CharField(max_length=200, blank=True, null=True)
    car_image = models.ImageField(null=True, blank=True)
    gaurantor1_name = models.CharField(max_length=200, blank=True, null=True)
    gaurantor1_phone = models.CharField(max_length=200, blank=True, null=True)
    gaurantor1_email = models.CharField(max_length=200, blank=True, null=True)
    gaurantor1_nin = models.CharField(max_length=200, blank=True, null=True)

    gaurantor2_name = models.CharField(max_length=200, blank=True, null=True)
    gaurantor2_phone = models.CharField(max_length=200, blank=True, null=True)
    gaurantor2_email = models.CharField(max_length=200, blank=True, null=True)
    gaurantor2_nin = models.CharField(max_length=200, blank=True, null=True)
    late_pay_total = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)

    car_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    backup_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    loan_balance = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    amount_per_week = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    no_weeks = models.IntegerField(null=True, blank=True, default=0)
    no_years = models.IntegerField(null=True, blank=True, default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    interest = models.DecimalField(null=True, max_digits=20, decimal_places=1, blank=True, default=0)

    rate = models.DecimalField(null=True, max_digits=20, decimal_places=0, blank=True, default=0)
    total_interest = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    Total_paid_so_far = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    notes = models.TextField(max_length=1000, blank=True, null=True, default='')
    cal_amount_remaining = models.IntegerField(null=True, blank=True, default=0)

    createdAt = models.DateTimeField(auto_now_add=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name


class LoanSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    paid_on = models.DateField(blank=True, null=True)
    expected_install_amt = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    amount_paid = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    balance = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    interest_rate = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    late_pay_charge = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0)
    status = models.CharField(max_length=200, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deposit_date = models.DateField(blank=True, null=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    loan_schedule_id = models.ForeignKey(LoanSchedule, on_delete=models.SET_NULL, null=True)
    amount_paid = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    balance = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    expected_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    payment_method = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    payment_for_dates = models.CharField(max_length=200, blank=True, null=True)
    interest = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True, default=0.00)
    createdAt = models.DateTimeField(auto_now_add=True)


class FailedPaymentLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True)
    amount_failed = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)
    balance = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)
    trans_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
