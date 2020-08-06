from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.customer.customer import CustomerForm
from pis_com.forms.ledger.ledger import LedgerForm
from pis_com.models import Customer


class AddNewLedger(FormView):
    form_class = CustomerForm
    template_name = 'ledger/create_ledger.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(AddNewLedger, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        customer = form.save()
        ledger_form_kwargs = {
            'retailer': self.request.POST.get('retailer'),
            'customer': customer.id,
            'person':self.request.POST.get('customer_type'),
            'amount': self.request.POST.get('amount'),
            'payment_amount': self.request.POST.get('payment_amount'),
            'payment_type': self.request.POST.get('payment_type'),
            'description': self.request.POST.get('description'),
        }

        ledger_form = LedgerForm(ledger_form_kwargs)
        if ledger_form.is_valid():
            ledger_form.save()

        return HttpResponseRedirect(reverse('customer_ledger_list'))

    def form_invalid(self, form):
        return super(AddNewLedger, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddNewLedger, self).get_context_data(**kwargs)
        customers = Customer.objects.filter(
            retailer=self.request.user.retailer_user.retailer)

        context.update({
            'customers': customers
        })

        return context
