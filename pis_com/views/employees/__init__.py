from django.urls import re_path

from .newemployee import AddNewEmployee
from .listview import EmployeeListView
from .deleteemployee import EmployeeDelete
from.salary import EmployeeSalaryView
from .salarydetail import EmployeeSalaryDetail

urlpatterns = [
    re_path(r'^add/new/employee$', AddNewEmployee.as_view(), name='add_new_employee'),
    re_path(r'^list/employee/$', EmployeeListView.as_view(),name='employee_list'),
    re_path(r'delete/employee/(?P<pk>\d+)/$',EmployeeDelete.as_view(),name='delete_employee'),
    re_path(r'salary/employee/(?P<pk>\d+)/$',EmployeeSalaryView.as_view(),name='employee_salary'),
    re_path(r'salary/employee/(?P<pk>\d+)/detail/$',EmployeeSalaryDetail.as_view(),name='employee_salary_detail'),
]
