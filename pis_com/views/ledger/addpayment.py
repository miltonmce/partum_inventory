from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.ledger.ledger import LedgerForm


class AddPayment(FormView):
    template_name = 'ledger/add_payment.html'
    form_class = LedgerForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(AddPayment, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        ledger = form.save()
        return HttpResponseRedirect(
            reverse('customer_ledger_detail', kwargs={
                'customer_id': self.kwargs.get('customer_id')
            })
        )

    def form_invalid(self, form):
        return super(AddPayment, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddPayment, self).get_context_data(**kwargs)
        try:
            customer = (
                self.request.user.retailer_user.retailer.
                retailer_customer.get(id=self.kwargs.get('customer_id'))
            )
        except ObjectDoesNotExist:
            raise Http404('Customer not found with concerned User')

        context.update({
            'customer': customer
        })
        return context
