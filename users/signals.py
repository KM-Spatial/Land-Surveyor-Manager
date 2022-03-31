from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Billing

from datetime import datetime, timedelta, date


# Signal To Create a User-Profile on Account Creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Signal to Create a 7-Day Trial on Account Creation
@receiver(post_save, sender=User)
def create_free_trial(sender, instance, created, **kwargs):
    if created:
        Billing.objects.create(user=instance, email=instance, phone='0776887606',
                               paid_on=datetime.now(),
                               amount=0,
                               payment_method='ecocash',
                               expire_date=date.today() + timedelta(days=15),  # -> Assign 7 Day Trial
                               reference_code='free_trial'
                               )


@receiver(post_save, sender=User)
def save_free_trial(sender, instance, **kwargs):
    instance.profile.save()
