from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from pis_com.models import Product


class ProductDetailsAPIView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            ProductDetailsAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            product_item = Product.objects.get(
                bar_code=self.request.POST.get('code'))
        except Product.DoesNotExist:
            return JsonResponse({
                'status': False,
                'message': 'Item with not exists',
            })

        latest_stock = product_item.stockin_product.all().latest('id')

        all_stock = product_item.stockin_product.all()
        if all_stock:
            all_stock = all_stock.aggregate(Sum('quantity'))
            all_stock = float(all_stock.get('quantity__sum') or 0)
        else:
            all_stock = 0

        purchased_stock = product_item.stockout_product.all()
        if purchased_stock:
            purchased_stock = purchased_stock.aggregate(
                Sum('stock_out_quantity'))
            purchased_stock = float(
                purchased_stock.get('stock_out_quantity__sum') or 0)
        else:
            purchased_stock = 0

        return JsonResponse({
            'status': True,
            'message': 'Success',
            'product_id': product_item.id,
            'product_name': product_item.name,
            'product_brand': product_item.brand_name,
            'product_price': '%g' % latest_stock.price_per_item,
            'stock': '%g' % (all_stock - purchased_stock)
        })
