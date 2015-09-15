from django.contrib import admin

from .models import (UserStripe, EmailMarketingSignup, UserAddress,
                     UserDefaultAddress, LessonCount)

# Register your models here.


class UserStripeAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user', '__unicode__']

    class Meta:
        model = UserStripe

admin.site.register(UserStripe, UserStripeAdmin)


class UserAddressAdmin(admin.ModelAdmin):
    search_fields = ['user', 'get_address']
    list_display = ['user', 'get_address']

    class Meta:
        model = UserAddress

admin.site.register(UserAddress, UserAddressAdmin)


class UserDefaultAddressAdmin(admin.ModelAdmin):
    search_fields = ['user', 'shipping', 'billing']
    list_display = ['user', 'shipping', 'billing']

    class Meta:
        model = UserDefaultAddress

admin.site.register(UserDefaultAddress, UserDefaultAddressAdmin)


class LessonCountAdmin(admin.ModelAdmin):
    search_fields = ['__unicode__']
    list_display = ['__unicode__', 'lesson_current_amount']
    list_editable = ['lesson_current_amount']

    class Meta:
        model = LessonCount

admin.site.register(LessonCount, LessonCountAdmin)


class EmailMarketingSignupAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp']

    class Meta:
        model = EmailMarketingSignup

admin.site.register(EmailMarketingSignup, EmailMarketingSignupAdmin)
