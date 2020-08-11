from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import FormView

from pis_com.forms.sales.billing import BillingForm
from pis_com.models.saleshistory import SalesHistory


class UpdateInvoiceView(FormView):
    template_name = 'sales/update_invoice.html'
    form_class = BillingForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            UpdateInvoiceView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateInvoiceView, self).get_context_data(**kwargs)
        products = (
            self.request.user.retailer_user.retailer.
                retailer_product.all()
        )
        customers = (
            self.request.user.retailer_user.
                retailer.retailer_customer.all()
        )
        invoice = SalesHistory.objects.get(id=self.kwargs.get('id'))
        context.update({
            'products': products,
            'customers': customers,
            'present_date': timezone.now().date(),
            'invoice': invoice
        })
        return context
