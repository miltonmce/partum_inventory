from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import TemplateView


class ProductDetailList(TemplateView):
    template_name = 'products/item_details.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(
            ProductDetailList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailList, self).get_context_data(**kwargs)
        try:
            product = (
                self.request.user.retailer_user.retailer.
                retailer_product.get(id=self.kwargs.get('pk'))
            )
        except ObjectDoesNotExist:
            raise Http404('Product not found with concerned User')

        context.update({
            'items_details': product.product_detail.all().order_by(
                '-created_at'),
            'product': product,
        })

        return context
