from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_SHOP = 'shop'
    USER_TYPE_COMPANY = 'company'
    USER_TYPE_INDIVIDUAL = 'individual'

    USER_TYPES = (
        (USER_TYPE_SHOP, 'Shop'),
        (USER_TYPE_COMPANY, 'Company'),
        (USER_TYPE_INDIVIDUAL, 'Individual'),
    )

    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=100, choices=USER_TYPES, default=USER_TYPE_SHOP
    )
    address = models.TextField(max_length=512, blank=True, null=True)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    mobile_no = models.CharField(max_length=13, blank=True, null=True)
    picture = models.ImageField(
        upload_to='images/profile/picture/', max_length=1024, blank=True
    )
    date_of_birth = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username
