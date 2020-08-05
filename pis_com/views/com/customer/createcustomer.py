from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse
from pis_com.forms.customer.customer import CustomerForm
from pis_com.models import Customer


class CreateCustomer(FormView):
    form_class = CustomerForm
    template_name = 'customer/create_customer.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            CreateCustomer, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('customers'))

    def form_invalid(self, form):
        return super(CreateCustomer, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(
            CreateCustomer, self).get_context_data(**kwargs)

        customers = Customer.objects.filter(
            retailer=self.request.user.retailer_user.retailer.id)
        context.update({
            'customers': customers
        })
        return context