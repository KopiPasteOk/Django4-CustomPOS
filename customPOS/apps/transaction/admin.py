from django.contrib import admin

from .models import TransactionItem, Transaction

class ItemLIne(admin.TabularInline):
    model = TransactionItem

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("trans_no", "trans_type", "create_by", "payment_type", "payment_term", "payment_amount", "payment_change")
    inlines = (ItemLIne,)

admin.site.register(Transaction, TransactionAdmin)

# admin.site.register(Item)
