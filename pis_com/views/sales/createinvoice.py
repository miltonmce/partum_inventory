from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import FormView

from pis_com.forms.sales.billing import BillingForm


class CreateInvoiceView(FormView):
    template_name = 'sales/create_invoice.html'
    form_class = BillingForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            CreateInvoiceView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateInvoiceView, self).get_context_data(**kwargs)
        products = (
            self.request.user.retailer_user.retailer.
                retailer_product.all()
        )
        customers = (
            self.request.user.retailer_user.
                retailer.retailer_customer.all()
        )
        context.update({
            'products': products,
            'customers': customers,
            'present_date': timezone.now().date(),
        })
        return context
