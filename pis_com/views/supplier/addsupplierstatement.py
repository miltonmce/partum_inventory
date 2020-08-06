from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.supplier.supplierstatement import SupplierStatementForm
from pis_com.models.supplier import Supplier


class AddSupplierStatement(FormView):
    form_class = SupplierStatementForm
    template_name = 'supplier/add_supplier_statement.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            AddSupplierStatement, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        obj.supplier = Supplier.objects.get(id=self.kwargs.get('pk'))
        obj.save()
        return HttpResponseRedirect(reverse(
            'list_supplier_statement',kwargs={
                'pk':obj.supplier.id}))

    def form_invalid(self, form):
        print(form.errors)
        return super(AddSupplierStatement, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddSupplierStatement, self).get_context_data(**kwargs)
        supplier = Supplier.objects.get(id=self.kwargs.get('pk'))

        context.update({
            'supplier': supplier
        })
        return context
