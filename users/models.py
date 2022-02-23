import random
import string
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.db import models

PROVINCE = (
    ('harare', 'Harare'), ('bulawayo', 'Bulawayo'), ('midlands', 'Midlands'), ('manicaland', 'Manicaland'),
    ('masvingo', 'Masvingo'), ('mash_east', 'Mashonaland East'), ('mash_west', 'Mashonaland West'),
    ('mash_central', 'Mashonaland Central'), ('mat_north', 'Matabeleland North'), ('mat_south', 'Matabeleland South'),
)

PAYMENT_METHOD = (
    ('ecocash', 'Ecocash'), ('onemoney', 'OneMoney'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default/default_profile_image.png', upload_to='profile_pics')
    org_name = models.CharField(max_length=100, verbose_name='Organization Name', null=True, blank=True)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    province = models.CharField(max_length=20, choices=PROVINCE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'User Profiles'


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=10, primary_key=True)
    description = models.TextField()
    discount_percentage = models.FloatField()

    def __str__(self):
        return self.coupon_code

    class Meta:
        verbose_name_plural = 'Coupons'


class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=10, help_text='Mobile Number - (e.g. 0776887606')
    paid_on = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    expire_date = models.DateField()
    reference_code = models.TextField()
    # PayNow Variables
    poll_url = models.TextField(null=True)
    payment_status = models.TextField(null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Billing Information'

    def save(self, *args, **kwargs):
        # Set an expiry date 30 days after payment
        self.expire_date = date.today() + timedelta(days=30)
        # Generate random string for reference code
        self.reference_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        super().save(*args, **kwargs)

    # TODO: Get Absolute URL here for the transaction details
