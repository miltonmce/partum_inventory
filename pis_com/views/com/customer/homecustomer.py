from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse

class CustomerTemplateView(TemplateView):
    template_name = 'customer/customer_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            CustomerTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            CustomerTemplateView, self).get_context_data(**kwargs)

        customers = (
            self.request.user.retailer_user.retailer.
            retailer_customer.all().order_by('customer_name'))
        context.update({
            'customers': customers
        })
        return context
