from django.db import models

from pis_com.models.supplier import Supplier


class SupplierStatement(models.Model):
    supplier = models.ForeignKey(
        Supplier, related_name='supplier',
        null=True, blank=True,on_delete=models.CASCADE
                                 )
    supplier_amount = models.DecimalField(
        max_digits=100, decimal_places=2, null=True, blank=True, default=0)
    payment_amount = models.DecimalField(
        max_digits=100, decimal_places=2, null=True, blank=True, default=0)
    description = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.supplier.name if self.supplier else ''

    def remaining_amount(self):
        return self.supplier_amount - self.payment_amount
