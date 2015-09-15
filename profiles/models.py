from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from allauth.account.signals import user_logged_in, user_signed_up

from localflavor.us.models import PhoneNumberField
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField

from .signals import (membership_lesson_update, membership_lesson_completed,
                      membership_lesson_canceled)

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.


class EmailMarketingSignup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.email)


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username


def stripe_callback(sender, request, user, **kwargs):
    user_stripe_account, created = UserStripe.objects.get_or_create(user=user)
    if created:
        print "created for {}".format(user.username)

    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()

user_signed_up.connect(stripe_callback)
user_logged_in.connect(stripe_callback)


class UserDefaultAddress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    shipping = models.ForeignKey("UserAddress", null=True, blank=True,
                                 related_name="user_address_shipping_default")
    billing = models.ForeignKey("UserAddress", null=True, blank=True,
                                related_name="user_address_billing_default")

    def __unicode__(self):
        return str(self.user.username)


class UserAddressManager(models.Manager):
    def get_billing_addresses(self, user):
        return super(UserAddressManager, self).filter(billing=True, user=user)


class UserAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default="USA")
    state = USStateField()
    zipcode = USZipCodeField()
    phone = PhoneNumberField()
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.get_address()

    def get_address(self):
        return "{}, {}, {}, {}, {}, {}".format(self.name, self.address,
                                               self.city, self.state,
                                               self.country, self.zipcode)

    objects = UserAddressManager()

    class Meta:
        ordering = ['-updated', '-timestamp']


class LessonCount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    lesson_current_amount = models.PositiveIntegerField(
        default=0, verbose_name='Current Number of Lessons')

    def __unicode__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-user']

    def update_lesson_count(self):
        if self.lesson_current_amount > 0:
            self.user.is_member = True
            self.user.save()
        elif self.lesson_current_amount <= 0:
            self.user.is_member = False
            self.user.save()
        else:
            pass


def update_lesson_status(sender, instance, created, **kwargs):
    if not created:
        instance.update_lesson_count()


post_save.connect(update_lesson_status, sender=LessonCount)


def update_lessons_count(sender, new_lesson_count, **kwargs):
    lessoncount = sender
    current_lesson_amount = lessoncount.lesson_current_amount
    if current_lesson_amount >= 0:
        lessoncount.lesson_current_amount = current_lesson_amount + new_lesson_count
        lessoncount.save()

membership_lesson_update.connect(update_lessons_count)


def completed_lesson_removal(sender, new_lesson_count, **kwargs):
    lessoncount = sender
    current_lesson_amount = lessoncount.lesson_current_amount
    if current_lesson_amount >= 0:
        lessoncount.lesson_current_amount = new_lesson_count
        lessoncount.save()

membership_lesson_completed.connect(completed_lesson_removal)


def canceled_lesson_count(sender, new_lesson_count, **kwargs):
    lessoncount = sender
    current_lesson_amount = lessoncount.lesson_current_amount
    if current_lesson_amount >= 0:
        lessoncount.lesson_current_amount = new_lesson_count
        lessoncount.save()

membership_lesson_canceled.connect(canceled_lesson_count)


def user_logged_in_signal(sender, signal, request, user, **kwargs):
    request.session.set_expiry(80000)
    membership_obj, created = LessonCount.objects.get_or_create(user=user)
    if created:
        try:
            # amount of purchased lessons
            membership_obj.lesson_current_amount = new_lesson_count
            membership_obj.save()
            user.is_member = True
            user.save()
        except:
            # amount of purchased lessons
            membership_obj.lesson_current_amount = 0
            membership_obj.save()
            user.is_member = False
            user.save()
    user.lessoncount.update_lesson_count()

user_logged_in.connect(user_logged_in_signal)
