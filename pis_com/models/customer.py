from django.db import models


class Customer(models.Model):
    retailer = models.ForeignKey(
        'pis_com.Retailer',
        related_name='retailer_customer',
        on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    customer_type=models.CharField(max_length=200, default='customer', blank=True, null=True)
    address = models.TextField(max_length=500, blank=True,null=True)
    shop = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.customer_name
