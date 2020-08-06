from django.urls import reverse_lazy
from django.views.generic import DeleteView

from pis_com.models import Employee


class EmployeeDelete(DeleteView):
    model= Employee
    success_url= reverse_lazy('employee_list')
    success_message=''

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)