from decimal import Decimal
from django.db import models
from django.conf import settings

from products.models import Product, Variation

# Create your models here.

try:
	tax_rate = settings.DEFAULT_TAX_RATE
except Exception, e:
	raise NotImplementedError(str(e))

class Cart(models.Model):
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)	
	tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
	final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	number_of_lessons = models.DecimalField(default=1, max_digits=100, decimal_places=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Cart id: %s" %(self.id)
		
	def get_lesson_final_amount(self):
		instance = Cart.objects.get(id=self.id)
		final_number_of_lessons = Decimal(self.number_of_lessons)
		instance.number_of_lessons = final_number_of_lessons
		instance.save()
		return instance.number_of_lessons

	def get_tax_total_amount(self):
		instance = Cart.objects.get(id=self.id)
		two_places = Decimal(10) ** -2
		tax_rate_dec = Decimal("%s" %(tax_rate))
		sub_total_dec = Decimal(self.total)
		tax_total_dec = Decimal(tax_rate_dec * sub_total_dec).quantize(two_places)
		instance.tax_total = tax_total_dec
		instance.save()
		return instance.tax_total

	def get_final_amount(self):
		instance = Cart.objects.get(id=self.id)
		two_places = Decimal(10) ** -2
		tax_rate_dec = Decimal("%s" %(tax_rate))
		sub_total_dec = Decimal(self.total)
		tax_total_dec = Decimal(tax_rate_dec * sub_total_dec).quantize(two_places)
		instance.tax_total = tax_total_dec
		instance.final_total = sub_total_dec + tax_total_dec
		instance.save()
		return instance.final_total


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, null=True, blank=True)
	product = models.ForeignKey(Product)
	variations = models.ManyToManyField(Variation, null=True, blank=True)
	quantity = models.PositiveIntegerField(default=1)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	notes = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return "Cart id: %s" %str(self.cart.id)
		except:
			return self.product.title




			