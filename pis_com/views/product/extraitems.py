from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from pis_com.models import ExtraItems


class ExtraItemsView(TemplateView):
    template_name = 'products/purchased_extraitems.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(ExtraItemsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ExtraItemsView, self).get_context_data(**kwargs)
        extra_products = ExtraItems.objects.filter(
            retailer=self.request.user.retailer_user.retailer
        )

        context.update({
            'purchased_extra_items': extra_products
        })

        return context
