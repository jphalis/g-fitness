from django.contrib import admin

from .models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
	search_fields = ['__unicode__']
	list_display =['__unicode__', 'total', 'timestamp', 'updated', 'active']
	list_editable =['active']
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
	search_fields = ['__unicode__', 'product']
	list_display = ['__unicode__', 'product', 'quantity', 'line_total', 'timestamp', 'updated']
	class Meta:
		model = CartItem

admin.site.register(CartItem, CartItemAdmin)