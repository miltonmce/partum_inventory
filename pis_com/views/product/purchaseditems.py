from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from pis_com.models import PurchasedProduct


class PurchasedItems(TemplateView):
    template_name = 'products/purchased_items.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(PurchasedItems, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PurchasedItems, self).get_context_data(**kwargs)
        purchased_product = PurchasedProduct.objects.filter(
            product__retailer=self.request.user.retailer_user.retailer
        ).order_by('-created_at')

        context.update({
            'purchased_products': purchased_product
        })

        return context
