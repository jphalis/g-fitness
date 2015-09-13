from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^about/$', 'profiles.views.about', name='about'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^clients/$', 'profiles.views.clients', name='clients'),
    url(r'^contact/$', 'contact.views.home', name='contact'),
    url(r'^orders/$', 'orders.views.orders', name='user_orders'),
    url(r'^orders/history/$', 'orders.views.billing_history', name='history'),
    url(r'^ajax/dismiss_marketing_message/$', 'marketing.views.dismiss_marketing_message', name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', 'marketing.views.email_signup', name='ajax_email_signup'),
    url(r'^ajax/add_user_address/$', 'profiles.views.add_user_address', name='ajax_add_user_address'),
    url(r'^lessons/$', 'products.views.products', name='products'),
    url(r'^lessons/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
    url(r'^media/$', 'marketing.views.media', name='media'),
    url(r'^pricing/$', 'profiles.views.pricing', name='pricing'),
    url(r'^profile/$', 'profiles.views.user_profile', name='profile'),
    url(r'^required_forms/$', 'profiles.views.required_forms', name='required_forms'),
    # url(r'^s/$', 'products.views.search', name='search'),
    url(r'^search/$', 'profiles.views.search', name='search'),
    url(r'^services/$', 'profiles.views.services', name='services'),
    url(r'^settings/$', 'profiles.views.settings', name='settings'),
    url(r'^staff/$', 'profiles.views.staff', name='staff'),
    url(r'^workout_schedule/$', 'profiles.views.workout_schedule', name="workout_schedule"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/address/add/$', 'profiles.views.add_user_address', name='add_user_address'),
    url(r'^', include('schedule.urls')),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIAFILES_DIRS)

# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)