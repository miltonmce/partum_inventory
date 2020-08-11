from django.urls import reverse_lazy
from django.views.generic import UpdateView

from pis_com.forms.product.product import ProductForm
from pis_com.models import Product


class ProductUpdateView(UpdateView):
    template_name = 'products/update_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('stock_items_list')
