# Generated by Django 4.1 on 2022-08-22 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_beneficiary', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('nin_number', models.CharField(blank=True, max_length=200, null=True)),
                ('mtn_number', models.CharField(blank=True, max_length=200, null=True)),
                ('airtel_number', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('reg_number', models.CharField(blank=True, max_length=200, null=True)),
                ('chassis', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.IntegerField(blank=True, default=0, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('gaurantor1_name', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor1_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor1_email', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor1_nin', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor2_name', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor2_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor2_email', models.CharField(blank=True, max_length=200, null=True)),
                ('gaurantor2_nin', models.CharField(blank=True, max_length=200, null=True)),
                ('late_pay_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('car_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('backup_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('loan_balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('amount_per_week', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('no_weeks', models.IntegerField(blank=True, default=0, null=True)),
                ('no_years', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('interest', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=20, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, null=True)),
                ('total_interest', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('Total_paid_so_far', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('notes', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('cal_amount_remaining', models.IntegerField(blank=True, default=0, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('paid_on', models.DateField(blank=True, null=True)),
                ('expected_install_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('interest_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('late_pay_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('deposit_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('expected_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_for_dates', models.CharField(blank=True, max_length=200, null=True)),
                ('interest', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('loan_schedule_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.loanschedule')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FailedPaymentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_failed', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('trans_id', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.transaction')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]