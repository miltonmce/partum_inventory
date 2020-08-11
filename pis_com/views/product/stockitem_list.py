from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from pis_com.models import Product


class StockItemList(ListView):
    template_name = 'products/stock_list.html'
    model = Product
    paginate_by = 150
    ordering = 'name'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(
            StockItemList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = (
                self.request.user.retailer_user.retailer
                    .retailer_product.all()
            )

        if self.request.GET.get('name'):
            queryset = queryset.filter(
                name__icontains=self.request.GET.get('name'))

        return queryset.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(StockItemList, self).get_context_data(**kwargs)
        context.update({
            'search_value_name': self.request.GET.get('name')
        })
        return context
