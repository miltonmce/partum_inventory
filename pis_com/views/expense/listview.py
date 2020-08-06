from django.views.generic import ListView

from pis_com.models import ExtraExpense


class ExpenseListView(ListView):
    template_name = 'expense/expense_list.html'
    model = ExtraExpense
    paginate_by = 150
    is_paginated = True

    def get_queryset(self):
        query_set = ExtraExpense.objects.all().order_by('-date')
        return query_set
