from django.db import models
from django.db.models import Sum

class Product(models.Model):
    UNIT_TYPE_KG = 'Kilogram'
    UNIT_TYPE_GRAM = 'Gram'
    UNIT_TYPE_LITRE = 'Litre'
    UNIT_TYPE_QUANTITY = 'Quantity'

    UNIT_TYPES = (
        (UNIT_TYPE_KG, 'Kilogram'),
        (UNIT_TYPE_GRAM, 'Gram'),
        (UNIT_TYPE_LITRE, 'Litre'),
        (UNIT_TYPE_QUANTITY, 'Quantity'),
    )
    unit_type = models.CharField(
        choices=UNIT_TYPES, default=UNIT_TYPE_QUANTITY,
        blank=True, null=True, max_length=200
    )
    name = models.CharField(max_length=100, unique=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    retailer = models.ForeignKey(
        'pis_retailer.Retailer',
        related_name='retailer_product',on_delete=models.CASCADE
    )
    bar_code = models.CharField(max_length=13, unique=True, blank=True,
                                null=True)

    def __unicode__(self):
        return self.name

    def total_items(self):
        try:
            obj_stock_in = self.stockin_product.aggregate(Sum('quantity'))
            stock_in = float(obj_stock_in.get('quantity__sum'))
        except:
            stock_in = 0

        return stock_in


    def product_available_items(self):
        try:
            obj_stock_in = self.stockin_product.aggregate(Sum('quantity'))
            stock_in = float(obj_stock_in.get('quantity__sum'))
        except:
            stock_in = 0

        try:
            obj_stock_out = self.stockout_product.aggregate(
                Sum('stock_out_quantity'))
            stock_out = float(obj_stock_out.get('stock_out_quantity__sum'))
        except:
            stock_out = 0
        return  stock_in - stock_out

    def product_purchased_items(self):
        try:
            obj_stock_out = self.stockout_product.aggregate(
                Sum('stock_out_quantity'))
            stock_out = float(obj_stock_out.get('stock_out_quantity__sum'))
        except:
            stock_out = 0
        return  stock_out

    def total_num_of_claimed_items(self):
        obj = self.claimed_product.aggregate(Sum('claimed_items'))
        return obj.get('claimed_items__sum')