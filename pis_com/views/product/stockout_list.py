from django.views.generic import ListView

from pis_com.models import StockOut, Product


class StockOutListView(ListView):
    template_name = 'products/stockout_list.html'
    paginate_by = 100
    model = StockOut
    ordering = '-id'

    def get_queryset(self, **kwargs):
        queryset = self.queryset
        if not queryset:
            queryset = StockOut.objects.all()

        queryset = queryset.filter(product=self.kwargs.get('product_id'))
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(StockOutListView, self).get_context_data(**kwargs)
        context.update({
            'product': Product.objects.get(id=self.kwargs.get('product_id'))
        })
        return context
