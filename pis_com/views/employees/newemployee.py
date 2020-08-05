from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.employee.employee import EmployeeForm
from pis_com.models import Customer


class AddNewEmployee(FormView):
    form_class = EmployeeForm
    template_name = "employee/create.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(AddNewEmployee, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
     form.save()

     return HttpResponseRedirect(reverse('employee:employee_list'))

    def form_invalid(self, form):
        return super(AddNewEmployee, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddNewEmployee, self).get_context_data(**kwargs)
        customers = Customer.objects.filter(
            retailer=self.request.user.retailer_user.retailer)

        context.update({
            'customers': customers
        })
        return context
