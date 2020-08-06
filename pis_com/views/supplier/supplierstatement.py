from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from pis_com.models.supplier import Supplier
from pis_com.models.supplierstatement import SupplierStatement


class SupplierStatementList(ListView):
    template_name = 'supplier/list_supplier_statement.html'
    model = SupplierStatement
    paginate_by = 100

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            SupplierStatementList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query_set = SupplierStatement.objects.filter(
            supplier__id=self.kwargs.get('pk')).order_by('-date')
        if self.request.GET.get('date'):
            query_set= query_set.filter(
                supplier__name__contains=self.request.GET.get('date')
            )
        return query_set

    def get_context_data(self, **kwargs):
        context = super(SupplierStatementList, self).get_context_data(**kwargs)
        supplier_statements = SupplierStatement.objects.filter(supplier__id=self.kwargs.get('pk'))
        supplier = (
            Supplier.objects.get(id=self.kwargs.get('pk'))
        )
        try:
            supplier_amounts = supplier_statements.aggregate(Sum('supplier_amount'))
            supplier_amounts = supplier_amounts.get('supplier_amount__sum') or 0
            payment_amounts = supplier_statements.aggregate(Sum('payment_amount'))
            payment_amounts = payment_amounts.get('payment_amount__sum') or 0
        except:
            supplier_amounts = 0
            payment_amounts = 0

        supplier_total_remaining_amount = supplier_amounts - payment_amounts

        context.update({
            'supplier': supplier,
            'supplier_total_remaining_amount':supplier_total_remaining_amount
        })
        return context
