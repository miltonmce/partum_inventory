from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

from pis_com.forms.supplier.supplierstatement import SupplierStatementForm
from pis_com.models.supplier import Supplier
from pis_com.models.supplierstatement import SupplierStatement


class SupplierStatementUpdate(UpdateView):
    template_name = 'supplier/update_supplier_statement.html'
    model = SupplierStatement
    form_class = SupplierStatementForm

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(
            reverse('list_supplier_statement', kwargs={'pk':obj.supplier.id})
        )

    def form_invalid(self, form):
        return super(SupplierStatementUpdate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(SupplierStatementUpdate, self).get_context_data(**kwargs)
        supplier = (
            Supplier.objects.get(supplier__id=self.kwargs.get('pk'))
        )
        context.update({
            'supplier': supplier
        })
        return context
