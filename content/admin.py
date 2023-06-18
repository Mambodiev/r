from django.contrib import admin
from . import models
from .models import Course, Video, Pricing, Subscription, Store

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created')


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription, SubscriptionAdmin)
