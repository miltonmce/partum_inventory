from django.db import models
from .product import Product
from utils.metamodels.datedmodel import DatedModel
class ClaimedProduct(DatedModel):
    product = models.ForeignKey(Product, related_name='claimed_product',on_delete=models.CASCADE)
    customer = models.ForeignKey(
        'pis_com.Customer', related_name='customer_claimed_items',
        null=True, blank=True,on_delete=models.CASCADE
    )
    claimed_items = models.IntegerField(
        default=1, verbose_name='No. of Claimed Items')
    claimed_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True)

    def __unicode__(self):
        return self.product.name