from django.db import models

from pis_com.models import DatedModel


class ExtraItems(DatedModel):
    retailer = models.ForeignKey(
        'pis_com.Retailer', related_name='retailer_extra_items',on_delete=models.CASCADE
    )
    item_name = models.CharField(
        max_length=100, blank=True, null=True)
    quantity = models.CharField(
        max_length=100, blank=True, null=True)
    price = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True)
    discount_percentage = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True)
    total = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True)

    def __unicode__(self):
        return self.item_name or ''
