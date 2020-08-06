from django.db import models
from django.db.models import Sum


class Supplier(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=250, null= True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def supplier_remaining_amount(self):
        supplier_statement = self.supplier.all()
        try:
            total_amount = supplier_statement.aggregate(Sum('supplier_amount'))
            total_amount = total_amount.get('supplier_amount__sum') or 0
            total_payments = supplier_statement.aggregate(Sum('payment_amount'))
            total_payments = total_payments.get('payment_amount__sum') or 0
        except:
            total_amount = 0
            total_payments = 0

        return total_amount - total_payments
