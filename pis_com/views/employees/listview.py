from django.views.generic import ListView

from pis_com.models import Employee


class EmployeeListView(ListView):
    template_name = 'employee/employee_list.html'
    model = Employee
    paginate_by = 150
    is_paginated = True

    def get_queryset(self):
        query_set = Employee.objects.all().order_by('-date_of_joining')
        return query_set