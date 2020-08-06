from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.employee.salary import EmployeeSalaryForm
from pis_com.models import Employee


class EmployeeSalaryView(FormView):
    form_class = EmployeeSalaryForm
    template_name = 'employee/employee_salary.html'

    def form_valid(self, form):
       obj=form.save()
       obj.employee=Employee.objects.get(id=self.kwargs.get('pk'))
       obj.save()
       return HttpResponseRedirect(reverse('employee_list'))

    def form_invalid(self, form):
        return super(EmployeeSalaryView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeSalaryView, self).get_context_data(**kwargs)
        employee = (
            Employee.objects.get(id=self.kwargs.get('pk'))
        )
        context.update({
            'employee': employee
        })
        return context