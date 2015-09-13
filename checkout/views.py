from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
	pub_key = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']

		try:
			customer = stripe.Customer.retrieve(customer_id)
			customer.cards.create(card=token)
			charge = stripe.Charge.create(
			    amount = 1000, # amount in cents, again
			    currency = "usd",
			    customer = customer,
			    description = "%s" %(request.user.email)
			)
		except stripe.CardError, e:
			# The card has been declined
			pass

	context = {'pub_key': pub_key}
	template = 'checkout.html'
	return render(request, template, context)