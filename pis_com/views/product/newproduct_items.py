from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.product.productdetails import ProductDetailsForm


class AddProductItems(FormView):
    template_name = 'products/add_product_items.html'
    form_class = ProductDetailsForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(AddProductItems, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        product_item_detail = form.save()
        return HttpResponseRedirect(
            reverse('item_details', kwargs={
                'pk': product_item_detail.product.id
            })
        )

    def form_invalid(self, form):
        return super(AddProductItems, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddProductItems, self).get_context_data(**kwargs)
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
