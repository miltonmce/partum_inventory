from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic.base import View


class ProductItemAPIView(View):

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            ProductItemAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        products = (
            self.request.user.retailer_user.retailer.
                retailer_product.all()
        )

        items = []

        for product in products:
            p = {
                'id': product.id,
                'name': product.name,
                'brand_name': product.brand_name,
            }

            if product.stockin_product.exists():
                stock_detail = product.stockin_product.all().latest('id')
                p.update({
                    'retail_price': stock_detail.price_per_item,
                    'consumer_price': stock_detail.price_per_item,
                })

                all_stock = product.stockin_product.all()
                if all_stock:
                    all_stock = all_stock.aggregate(Sum('quantity'))
                    all_stock = float(all_stock.get('quantity__sum') or 0)
                else:
                    all_stock = 0

                purchased_stock = product.stockout_product.all()
                if purchased_stock:
                    purchased_stock = purchased_stock.aggregate(
                        Sum('stock_out_quantity'))
                    purchased_stock = float(
                        purchased_stock.get('stock_out_quantity__sum') or 0)
                else:
                    purchased_stock = 0

                p.update({
                    'stock': all_stock - purchased_stock
                })

            else:
                p.update(
                    {
                        'retail_price': 0,
                        'consumer_price': 0
                    }
                )

            items.append(p)

        return JsonResponse({'products': items})
