from django.db.models import Sum
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import TemplateView

from pis_com.models import Customer


class CustomerLedgerDetailsView(TemplateView):
    template_name = 'ledger/customer_ledger_details.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            CustomerLedgerDetailsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            CustomerLedgerDetailsView, self).get_context_data(**kwargs)

        try:
            customer = Customer.objects.get(
                id=self.kwargs.get('customer_id')
            )
        except Customer.DoesNotExist:
            raise Http404

        ledgers = customer.customer_ledger.all()
        if ledgers:
            ledger_total = ledgers.aggregate(Sum('amount'))
            ledger_total = float(ledger_total.get('amount__sum'))
            context.update({

            })
        else:
            ledger_total = 0

        if ledgers:
            payment_total = ledgers.aggregate(Sum('payment'))
            payment_total = float(payment_total.get('payment__sum'))
            context.update({

            })
        else:
            payment_total = 0

        context.update({
            'customer': customer,
            'ledgers': ledgers.order_by('-dated'),
            'ledger_total': '%g' % ledger_total,
            'payment_total': '%g' % payment_total,
            'remaining_amount': '%g' % (ledger_total - payment_total)
        })

        return context
