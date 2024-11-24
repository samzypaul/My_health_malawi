from django.contrib import admin
from .models import Plan, SubscriptionCode

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_offer', 'description', 'price')  # Fields to display in the admin list view

@admin.register(SubscriptionCode)
class SubscriptionCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'plan', 'created_by', 'is_used', 'created_at')  # Customize as needed
    list_filter = ('is_used', 'plan')  # Filters for better admin usability
    search_fields = ('code',)
