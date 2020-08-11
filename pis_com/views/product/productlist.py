from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class ProductItemList(TemplateView):
    template_name = 'products/product_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(
            ProductItemList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductItemList, self).get_context_data(**kwargs)
        products = (
            self.request.user.retailer_user.retailer.retailer_product.all()
        )
        context.update({
            'products': products
        })
        return context
