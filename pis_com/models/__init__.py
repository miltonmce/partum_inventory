import random

from django.contrib.auth.models import User
from django.db.models.signals import post_save


from .adminconf import AdminConfiguration
from.customer import Customer
from .dated import DatedModel
from .feedback import FeedBack
from .user import UserProfile


from .employee import Employee
from .employeesalary import EmployeeSalary

from .expense import ExtraExpense

from .ledger import Ledger

from .retailer import Retailer
from .retaileruser import RetailerUser


from .product import Product
from .stockin import StockIn
from .productdetail import ProductDetail
from .purchased_product import PurchasedProduct
from .extraitems import ExtraItems
from .claimedproduct import ClaimedProduct
from .stockout import StockOut

from .saleshistory import SalesHistory



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


def int_to_bin(value):
        return bin(value)[2:]


def bin_to_int(value):
        return int(value, base=2)


# Signals Function for bar code
def create_save_bar_code(sender, instance, created, **kwargs):

    if not instance.bar_code:
        import time
        from pis_com import ean13

        code = None

        r = random.Random(time.time())
        m = int_to_bin(instance.pk % 4)
        if len(m) == 1:
            m = '0' + m
        elif not len(m):
            m = '00'

        while not code:
            g = ''.join([str(r.randint(0, 1)) for i in range(32)])
            chk = int_to_bin(bin_to_int(g) % 16)

            if len(chk) < 4:
                chk = '0' * (4 - len(chk)) + chk

            chk = ''.join(['1' if x == '0' else '0' for x in chk])

            if m == '11':
                code = ''.join(['1', m, g[:16], chk, g[16:32]])
            elif m == '10':
                code = ''.join(['1', m, g[:11], chk, g[11:32]])
            elif m == '01':
                code = ''.join(['1', m, g[:19], chk, g[19:32]])
            else:
                code = ''.join(
                    ['1', m, g[:9], chk[:2], g[9:23], chk[2:4], g[23:32]])

            code = '%d' % bin_to_int(code)
            code += '%d' % ean13.get_checksum(code)

        instance.bar_code = code
        instance.save()


# Signal Calls bar code
post_save.connect(create_save_bar_code, sender=Product)

# Signals
def purchase_product(sender, instance, created, **kwargs):
    """
    TODO: Zaheer Please check this function is useful or not.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    product_items = (
        instance.product.product_detail.filter(
            available_item__gt=0).order_by('created_at')
    )

    if product_items:
        item = product_items[0]
        item.available_item - 1
        item.save()


# Signals Function
def create_save_receipt_no(sender, instance, created, **kwargs):
    if created and not instance.receipt_no:
        while True:
            random_code = random.randint(1000000, 9999999)
            if (
                not SalesHistory.objects.filter(
                    receipt_no=random_code).exists()
            ):
                break

        instance.receipt_no = random_code
        instance.save()


# Signal Calls
post_save.connect(create_save_receipt_no, sender=SalesHistory)