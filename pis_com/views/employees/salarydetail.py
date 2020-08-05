from django.http import Http404
from django.views.generic import TemplateView

from pis_com.models import Employee
from pis_com.models.employeesalary import EmployeeSalary


class EmployeeSalaryDetail(TemplateView):
    template_name = 'employee/employee_salary_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            EmployeeSalaryDetail, self).get_context_data(**kwargs)

        try:
            salaries = EmployeeSalary.objects.filter(
                employee__id=self.kwargs.get('pk')
            )
        except Employee.DoesNotExist:
            raise Http404

        context.update({
            'salaries': salaries,
            'employee':Employee.objects.get(id=self.kwargs.get('pk'))

        })

        return context
