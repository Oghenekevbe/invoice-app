from django.contrib import admin
from .models import Customer, Invoice, Receipt, Profile

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'phone_number')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer', 'description','discount_percentage', 'amount', 'created_at', 'status')

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('customer', 'description','discount_percentage', 'amount', 'created_at')


admin.site.register(Profile)