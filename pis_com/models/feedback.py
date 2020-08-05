from django.db import models
from django.utils import timezone


class FeedBack(models.Model):
    retailer = models.ForeignKey(
        'pis_retailer.Retailer',
        related_name='retailer_feedback', null=True, blank=True,
        on_delete=models.CASCADE
    )
    description= models.CharField(max_length=200, null=True, blank=True)
    date=models.DateField(default=timezone.now, null=True, blank=True)

    def __unicode__(self):
        return self.description
