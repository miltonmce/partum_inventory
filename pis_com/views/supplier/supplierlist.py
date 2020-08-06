from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from pis_com.models.supplier import Supplier
from pis_com.models.supplierstatement import SupplierStatement


class SupplierList(ListView):
    template_name = 'supplier/list_supplier.html'
    model = Supplier
    paginate_by = 100

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            SupplierList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SupplierList, self).get_context_data(**kwargs)
        supplier_statements = SupplierStatement.objects.all()
        try:
            supplier_amounts = supplier_statements.aggregate(Sum('supplier_amount'))
            supplier_amounts = supplier_amounts.get('supplier_amount__sum') or 0
            payment_amounts = supplier_statements.aggregate(Sum('payment_amount'))
            payment_amounts = payment_amounts.get('payment_amount__sum') or 0
        except:
            supplier_amounts = 0
            payment_amounts = 0

        total_remaining_amount = supplier_amounts - payment_amounts
        context.update({
            'total_remaining_amount':total_remaining_amount
        })
        return context
