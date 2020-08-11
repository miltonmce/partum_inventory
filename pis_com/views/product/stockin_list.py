from django.views.generic import ListView

from pis_com.models import StockIn, Product


class StockInListView(ListView):
    template_name = 'products/stockin_list.html'
    paginate_by = 100
    model = StockIn
    ordering = '-id'

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = StockIn.objects.all()

        queryset = queryset.filter(product=self.kwargs.get('product_id'))
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(StockInListView, self).get_context_data(**kwargs)
        context.update({
            'product': Product.objects.get(id=self.kwargs.get('product_id'))
        })
        return context
