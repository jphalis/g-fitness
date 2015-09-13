from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

# Create your models here.

# class Category(models.Model):
# 	title = models.CharField(max_length=120)
# 	description = models.CharField(max_length=120, blank=True)
# 	slug = models.SlugField(unique=True)
# 	featured = models.BooleanField(default=None)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	active = models.BooleanField(default=True)

# 	def __unicode__(self):
# 		return self.title

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	# category = models.ManyToManyField(Category, null=True, blank=True)
	number_of_lessons = models.PositiveIntegerField(default=1)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=60.00)
	discount_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_number_of_lessons(self):
		return self.number_of_lessons

	def get_discount_price(self):
		return self.discount_price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})

class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/', null=True, blank=True)
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		return self.product.title

class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')

VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	)

class Variation(models.Model):
	product = models.ForeignKey(Product)
	# category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=120)
	image = models.ForeignKey(ProductImage, null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	objects = VariationManager()

	def __unicode__(self):
		return self.title

# def product_defaults(sender, instance, created, *args, **kwargs):
# 	if instance.update_defaults:
# 		categories = instance.category.all()
# 		for cat in categories:
# 			if cat.id == 1: #for t-shirts
# 				small_size = Variation.objects.get_or_create(product=instance, category='size', title='Small')
# 				medium_size = Variation.objects.get_or_create(product=instance, category='size', title='Medium')
# 				large_size = Variation.objects.get_or_create(product=instance, category='size', title='Large')
# 		instance.update_defaults = False
# 		instance.save()

# post_save.connect(product_defaults, sender=Product)




