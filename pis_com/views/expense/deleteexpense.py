from django.urls import reverse_lazy
from django.views.generic import DeleteView

from pis_com.models import ExtraExpense


class ExpenseDelete(DeleteView):
    model= ExtraExpense
    success_url= reverse_lazy('expense_list')
    success_message=''

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
