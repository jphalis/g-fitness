from django.contrib import admin

from .models import MarketingMessage, Slider, Media

# Register your models here.

class MarketingMessageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'start_date', 'end_date', 'active', 'featured']
	list_editable = ['active', 'featured']
	class Meta:
		model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)

class SliderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'order', 'start_date', 'end_date', 'redirect_url', 'active', 'featured']
	list_editable = ['order', 'redirect_url', 'active', 'featured']
	class Meta:
		model = Slider

admin.site.register(Slider, SliderAdmin)

class MediaAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'order', 'redirect_url', 'active']
	list_editable = ['order', 'redirect_url', 'active']
	class Meta:
		model = Media

admin.site.register(Media, MediaAdmin)