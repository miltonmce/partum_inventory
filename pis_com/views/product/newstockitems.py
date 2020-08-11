from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.product.stockdetails import StockDetailsForm


class AddStockItems(FormView):
    template_name = 'products/add_stock_item.html'
    form_class = StockDetailsForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(AddStockItems, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        product_item_detail = form.save()
        return HttpResponseRedirect(
            reverse('stock_items_list'
                    )
        )

    def form_invalid(self, form):
        return super(AddStockItems, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddStockItems, self).get_context_data(**kwargs)
        try:
            product = (
                self.request.user.retailer_user.retailer.
                retailer_product.get(id=self.kwargs.get('product_id'))
            )
        except ObjectDoesNotExist:
            raise Http404('Product not found with concerned User')

        context.update({
            'product': product
        })
        return context
