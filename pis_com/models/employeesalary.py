from django.db import models

from .employee  import Employee


class EmployeeSalary(models.Model):
    employee=models.ForeignKey(Employee, related_name='employee_salary',
                               null=True, blank=True,on_delete=models.CASCADE)
    salary_amount=models.CharField(max_length=100, null=True, blank=True)
    date=models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.employee
