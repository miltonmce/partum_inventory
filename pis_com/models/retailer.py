from django.db import models

from pis_com.models import DatedModel


class Retailer(DatedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=False)
    package = models.CharField(max_length=200, null=True, blank=True)
    package_price = models.CharField(max_length=200, null=True, blank=True)
    package_expiry = models.DateField(blank=True, null=True)
    logo = models.ImageField(
        upload_to='images/retailer/logo/', max_length=1024,
        blank=True, null=True
    )

    def __unicode__(self):
        return self.name
