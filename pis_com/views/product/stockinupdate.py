from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

from pis_com.forms.product.stockdetails import StockDetailsForm
from pis_com.models import StockIn


class StockInUpdateView(UpdateView):
    template_name = 'products/update_stockin.html'
    model = StockIn
    form_class = StockDetailsForm

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(
            reverse('stockin_list',
                    kwargs={'product_id': obj.product.id})
        )

    def form_invalid(self, form):
        return super(StockInUpdateView, self).form_invalid(form)
