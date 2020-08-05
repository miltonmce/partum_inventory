from django.contrib.auth.models import User
from django.db.models.signals import post_save


from .adminconf import AdminConfiguration
from.customer import Customer
from .dated import DatedModel
from .feedback import FeedBack
from .user import UserProfile


from .employee import Employee
from .employeesalary import EmployeeSalary






def create_profile(sender, instance, created, **kwargs):
    """
    The functions used to check if user profile is not created
    and created the user profile without saving role and hospital
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created and not UserProfile.objects.filter(user=instance):
        return UserProfile.objects.create(
            user=instance
        )


# Signals
post_save.connect(create_profile, sender=User)