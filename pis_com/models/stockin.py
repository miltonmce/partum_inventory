from django.db import models

from .product import Product


class StockIn(models.Model):
    product = models.ForeignKey(
        Product, related_name='stockin_product',on_delete=models.CASCADE
    )
    quantity = models.CharField(
        max_length=100, blank=True, null=True
    )
    price_per_item = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True,
        help_text="Selling Price for a Single Item"
    )
    total_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    buying_price_item = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True,
        help_text='Buying Price for a Single Item'
    )
    total_buying_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    dated_order = models.DateField(blank=True, null=True)
    stock_expiry = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.product.name
