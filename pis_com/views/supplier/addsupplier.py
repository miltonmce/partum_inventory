from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.supplier.supplier import SupplierForm


class AddSupplier(FormView):
    form_class = SupplierForm
    template_name = 'supplier/add_supplier.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            AddSupplier, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        return HttpResponseRedirect(reverse('list_supplier'))

    def form_invalid(self, form):
        return super(AddSupplier, self).form_invalid(form)
