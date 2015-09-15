import stripe

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

from profiles.forms import UserAddressForm
from profiles.models import UserAddress, LessonCount
from carts.models import Cart

from .models import Order
from profiles.signals import membership_lesson_update
from .utils import id_generator

# Create your views here.

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret = settings.STRIPE_SECRET_KEY
except Exception, e:
    print str(e)
    raise NotImplementedError(str(e))

stripe.api_key = stripe_secret


def orders(request):

    context = {}
    return render(request, 'orders/user.html', context)


@login_required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except Cart.DoesNotExist:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        new_order = None
        return HttpResponseRedirect(reverse("cart"))

    final_amount = 0
    final_lesson_count = 0

    if new_order is not None:
        new_order.sub_total = cart.total
        new_order.number_of_lessons = cart.number_of_lessons
        new_order.save()
        final_amount = new_order.get_final_amount()
        final_lesson_count = new_order.get_lesson_final_amount()

    try:
        address_added = request.GET.get("address_added")
    except:
        address_added = None

    if address_added is None:
        address_form = UserAddressForm()
    else:
        address_form = None

    current_addresses = UserAddress.objects.filter(user=request.user)
    billing_addresses = UserAddress.objects.get_billing_addresses(
        user=request.user)

    if request.method == "POST":
        try:
            user_stripe = request.user.userstripe.stripe_id
            customer = stripe.Customer.retrieve(user_stripe)
        except:
            customer = None
            pass
        if customer is not None:
            shipping_a = request.POST['shipping_address']
            billing_a = request.POST['billing_address']
            token = request.POST['stripeToken']

            try:
                shipping_address_instance = UserAddress.objects.get(
                    id=shipping_a)
            except:
                shipping_address_instance = None

            try:
                billing_address_instance = UserAddress.objects.get(
                    id=billing_a)
            except:
                billing_address_instance = None

            card = customer.cards.create(card=token)
            card.name = billing_address_instance.name or None
            card.address_city = billing_address_instance.city or None
            card.address_line1 = billing_address_instance.address or None
            card.address_line2 = billing_address_instance.address2 or None
            card.address_country = billing_address_instance.country or None
            card.address_state = billing_address_instance.state or None
            card.address_zip = billing_address_instance.zipcode or None
            card.save()

            charge = stripe.Charge.create(
                amount=int(final_amount * 100),
                currency="usd",
                card=card,  # obtained with Stripe.js
                customer=customer,
                receipt_email=request.user.email,
                description="Charge for {}".format(request.user.username)
            )
            if charge["captured"]:
                new_order.status = "Finished"
                new_order.shipping_address = shipping_address_instance
                new_order.billing_address = billing_address_instance
                new_order.save()
                membership_instance, created = LessonCount.objects \
                    .get_or_create(user=request.user)
                membership_lesson_update.send(
                    membership_instance,
                    new_lesson_count=new_order.number_of_lessons)
                del request.session['cart_id']
                del request.session['items_total']
                messages.success(
                    request, "Thank you! Your order has been completed!")
                return HttpResponseRedirect(reverse("user_orders"))

    context = {
        'order': new_order,
        'address_form': address_form,
        'current_addresses': current_addresses,
        'billing_addresses': billing_addresses,
        'stripe_pub': stripe_pub,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def billing_history(request):
    history = Order.objects.filter(user=request.user, status='Finished')
    return render(request, "orders/history.html", {"queryset": history})
