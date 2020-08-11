from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.product.product import ProductForm


class AddNewProduct(FormView):
    form_class = ProductForm
    template_name = 'products/add_product.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            AddNewProduct, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        product = form.save()

        return HttpResponseRedirect(reverse('stock_items_list'))

    def form_invalid(self, form):
        return super(AddNewProduct, self).form_invalid(form)
