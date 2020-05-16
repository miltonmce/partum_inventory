from django.db import models
from .product import Product
from utils.metamodels.datedmodel import DatedModel

class ProductDetail(DatedModel):
    product = models.ForeignKey(
        Product, related_name='product_detail',on_delete=models.CASCADE
    )
    retail_price = models.DecimalField(
        max_digits=65, decimal_places=2, default=0
    )
    consumer_price = models.DecimalField(
        max_digits=65, decimal_places=2, default=0
    )
    available_item = models.IntegerField(default=1)
    purchased_item = models.IntegerField(default=0)

    def __unicode__(self):
        return self.product.name