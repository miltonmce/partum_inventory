from django.contrib.auth.models import User
from django.db import models

from pis_com.models.retailer import Retailer


class RetailerUser(models.Model):
    ROLE_TYPE_OWNER = 'owner'
    ROLE_TYPE_DATA_ENTRY_USER = 'data_entry_user'
    ROLE_TYPE_SALESMAN = 'salesman'
    ROLE_TYPE_VIEW_ACCOUNT = 'account_viewer'
    ROLE_TYPE_LEDGER_VIEW = 'ledger_viewer'

    ROLE_TYPES = (
        (ROLE_TYPE_OWNER, 'Owner'),
        (ROLE_TYPE_DATA_ENTRY_USER, 'Data Entry User'),
        (ROLE_TYPE_SALESMAN, 'Salesman'),
        (ROLE_TYPE_VIEW_ACCOUNT, 'Account Viewer'),
        (ROLE_TYPE_LEDGER_VIEW, 'Ledger Viewer'),
    )

    user = models.OneToOneField(User, related_name='retailer_user',on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, related_name='u_retailer',on_delete=models.CASCADE)
    role_type = models.CharField(
        max_length=100, choices=ROLE_TYPES, default=ROLE_TYPE_OWNER
    )

    def __unicode__(self):
        return self.user.username
