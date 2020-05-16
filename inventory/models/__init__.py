
from .claimedproduct import ClaimedProduct
from .extraitems import ExtraItems
from .product import Product
from .productdetail import ProductDetail
from .purchasedproduct import PurchasedProduct
from .stockin import StockIn
from .stockout import StockOut


from django.db.models.signals import post_save


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