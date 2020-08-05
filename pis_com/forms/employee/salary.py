from django import forms
from pis_com.models.employeesalary import EmployeeSalary


class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'