from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from products.models import Product, Variation
from .models import Cart, CartItem

# Create your views here.

def view(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None

	if the_id:
		new_total = 0.00
		new_lesson_count = 0
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_total += line_total
			lesson_total = float(item.product.number_of_lessons)
			new_lesson_count += lesson_total
		request.session['items_total'] = cart.cartitem_set.count()
		cart.total = new_total
		cart.number_of_lessons = new_lesson_count
		cart.save()
		context = {'cart': cart}
	else:
		empty_message = "Your Cart is empty, please keep shopping."
		context = {
			'empty': True,
			'empty_message': empty_message
		}

	template = 'cart/view.html'
	return render(request, template, context)

def remove_from_cart(request, id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("cart"))

	cartitem = CartItem.objects.get(id=id)
	cartitem.cart = None
	cartitem.save()
	messages.warning(request, "You have removed this item from your cart.")
	return HttpResponseRedirect(reverse("cart"))

def add_to_cart(request, slug):
	request.session.set_expiry(600)

	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)
	
	try:
		product = Product.objects.get(slug=slug)
		messages.success(request, "1 item added to your cart!")
	except Product.DoesNotExist:
		pass
	except:
		pass

	product_var = [] #product variations
	if request.method == "POST":
		qty = request.POST.get("qty", 1)
		for item in request.POST:
			key = item
			value = request.POST[key]
			try:
				v = Variation.objects.get(product=product, category__iexact=key, title__iexact=value)
				product_var.append(v)
			except:
				pass
		cart_item = CartItem.objects.create(cart=cart, product=product)
		if len(product_var) > 0:
			cart_item.variations.add(*product_var)
		cart_item.quantity = qty
		cart_item.save()
		# success message
		return HttpResponseRedirect(reverse("cart"))
		# error message
	return HttpResponseRedirect(reverse("cart"))





