from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.urls import reverse
from pis_com.forms import CustomerForm
from pis_com.models import Customer


class CustomerUpdateView(UpdateView):
    form_class = CustomerForm
    template_name = 'customer/update_customer.html'
    model = Customer
    success_url = reverse_lazy('customers')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            CustomerUpdateView, self).dispatch(request, *args, **kwargs)