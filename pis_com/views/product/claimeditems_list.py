from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from pis_com.models import ClaimedProduct


class ClaimedItemsListView(TemplateView):
    template_name = 'products/claimed_product_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            ClaimedItemsListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            ClaimedItemsListView, self).get_context_data(**kwargs)
        context.update({
            'claimed_items': ClaimedProduct.objects.all().order_by(
                '-created_at')
        })
        return context
