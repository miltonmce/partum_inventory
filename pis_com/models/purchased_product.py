from django.db import models

from pis_com.models import DatedModel, Product


class PurchasedProduct(DatedModel):
    product = models.ForeignKey(
        Product, related_name='purchased_product',on_delete=models.CASCADE
    )
    invoice = models.ForeignKey(
        'pis_com.SalesHistory', related_name='purchased_invoice',
        blank=True, null=True,on_delete=models.CASCADE
    )
    quantity = models.DecimalField(
        max_digits=65, decimal_places=2, default=1, blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    discount_percentage = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    purchase_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    def __unicode__(self):
        return self.product.name
