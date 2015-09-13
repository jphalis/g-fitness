from django.contrib import admin
from .models import Product, ProductImage, Variation #Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	search_fields = ['title', 'description']
	list_display = ['title', 'number_of_lessons', 'price', 'discount_price', 'active', 'updated']
	list_editable = ['number_of_lessons', 'price', 'discount_price', 'active']
	list_filter = ['price', 'active']
	readonly_fields = ['updated', 'timestamp']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
	search_fields = ['product']
	list_display = ['product', 'featured', 'thumbnail', 'active', 'updated']
	list_editable = ['featured', 'thumbnail', 'active']
	list_filter = ['featured', 'thumbnail', 'active']

admin.site.register(ProductImage, ProductImageAdmin)

class VariationAdmin(admin.ModelAdmin):
	list_display = ['product', 'title', 'price', 'active', 'updated']
	list_editable = ['price', 'active',]

admin.site.register(Variation, VariationAdmin)

# admin.site.register(Category)