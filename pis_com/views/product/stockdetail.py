from django.http import Http404
from django.views.generic import TemplateView

from pis_com.models import Product, StockIn


class StockDetailView(TemplateView):
    template_name = 'products/stock_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            StockDetailView, self).get_context_data(**kwargs)

        try:
            item = Product.objects.get(id=self.kwargs.get('product_id'))
        except StockIn.DoesNotExist:
            return Http404('Item does not exists in database')

        item_stocks_in = item.stockin_product.all()
        item_stocks_out = item.stockout_product.all()

        context.update({
            'item': item,
            'item_stock_in': item_stocks_in.order_by('-dated_order'),
            'item_stock_out': item_stocks_out.order_by('-dated'),
        })

        return context
