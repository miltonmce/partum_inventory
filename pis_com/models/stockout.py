from django.db import models

from pis_com.models import DatedModel
from .purchased_product import PurchasedProduct
from .product import Product


class StockOut(models.Model):
    product = models.ForeignKey(
        Product, related_name='stockout_product',on_delete=models.CASCADE
    )
    invoice = models.ForeignKey(
        'pis_sales.SalesHistory', related_name='out_invoice',
        blank=True, null=True,on_delete=models.CASCADE
    )
    purchased_item = models.ForeignKey(
        PurchasedProduct, related_name='out_purchased',
        blank=True, null=True,on_delete=models.CASCADE
    )
    stock_out_quantity=models.CharField(max_length=100, blank=True, null=True)
    selling_price = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    buying_price = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    dated=models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.product.name
