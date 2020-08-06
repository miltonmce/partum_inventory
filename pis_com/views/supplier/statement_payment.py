from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.supplier.supplierstatement import SupplierStatementForm
from pis_com.models.supplier import Supplier


class StatementPayment(FormView):
    form_class = SupplierStatementForm
    template_name = 'supplier/payment.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            StatementPayment, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse(
            'list_supplier_statement', kwargs={
                'pk': self.kwargs.get('pk')}))

    def form_invalid(self, form):
        return super(StatementPayment, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(StatementPayment, self).get_context_data(**kwargs)
        supplier = (
            Supplier.objects.get(id=self.kwargs.get('pk'))
        )
        context.update({
            'supplier': supplier
        })
        return context