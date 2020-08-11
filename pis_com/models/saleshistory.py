from django.db import models

from pis_com.models import DatedModel


class SalesHistory(DatedModel):
    retailer = models.ForeignKey(
        'pis_com.Retailer', related_name='retailer_sales',on_delete=models.CASCADE
    )
    receipt_no = models.CharField(
        max_length=20, unique=True, blank=True, null=True
    )

    customer = models.ForeignKey(
        'pis_com.Customer',
        related_name='customer_sales',
        blank=True, null=True,on_delete=models.CASCADE
    )

    product_details = models.TextField(
        max_length=512, blank=True, null=True,
        help_text='Quantity and Product name would save in JSON format')

    purchased_items = models.ManyToManyField(
        'pis_com.PurchasedProduct',
        max_length=100, blank=True
    )

    extra_items = models.ManyToManyField(
        'pis_com.ExtraItems',
        max_length=200, blank=True,
    )

    total_quantity = models.CharField(
        max_length=10, blank=True, null=True, default=1)

    sub_total = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    paid_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    remaining_payment = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    discount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    shipping = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    grand_total = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    cash_payment = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    returned_payment = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    def __unicode__(self):
        return self.retailer.name
