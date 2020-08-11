from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from pis_com.models.saleshistory import SalesHistory


class InvoicesList(ListView):
    template_name = 'sales/invoice_list.html'
    model = SalesHistory
    paginate_by = 200

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(InvoicesList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = (
            self.request.user.retailer_user.retailer.
                retailer_sales.all().order_by('-created_at')
        )
        return queryset

    def get_sales_history(self):
        return (
            self.request.user.retailer_user.retailer.
                retailer_sales.all().order_by('-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super(InvoicesList, self).get_context_data(**kwargs)
        return context
