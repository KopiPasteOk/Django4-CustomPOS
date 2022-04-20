from django.db import models


class Transaction(models.Model):
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    trans_no = models.CharField(max_length=254)
    trans_type = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    payment_term = models.CharField(max_length=255, blank=True, null=True)
    payment_amount = models.DecimalField(max_length=100, blank=True, null=True, decimal_places=2, max_digits=9)
    payment_change = models.DecimalField(max_length=100, blank=True, null=True, decimal_places=2, max_digits=9)
    
    def __str__(self):
        return f"{self.trans_no}"
   
   
# class TransactionItem(models.Model):
#     class Meta:
#         verbose_name = 'Item'
#         verbose_name_plural = 'Items'

#     transaction = models.ForeignKey(
#         'transaction.Transaction', 
#         on_delete=models.CASCADE, 
#         related_name="items",
#         null=True
#     )
#     item_code = models.CharField(max_length=100)
#     item_id = models.CharField(max_length=100, blank=True, null=True)
#     qty = models.CharField(max_length=100, blank=True, null=True)
#     unit = models.CharField(max_length=100, blank=True, null=True)
#     price = models.CharField(max_length=100, blank=True, null=True)
#     tax = models.CharField(max_length=100, blank=True, null=True)
#     disc = models.CharField(max_length=100, blank=True, null=True)
    
    
#     def __str__(self):
#         return f'{self.transaction.id} - {self.item_code}' 
