from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.expense.extraexpense import ExtraExpenseForm
from pis_com.models import Customer


class AddNewExpense(FormView):
    form_class = ExtraExpenseForm
    template_name = 'expense/create_expense.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(AddNewExpense, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
     form.save()
     return HttpResponseRedirect(reverse('expense_list'))

    def form_invalid(self, form):
        return super(AddNewExpense, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddNewExpense, self).get_context_data(**kwargs)
        customers = Customer.objects.filter(
            retailer=self.request.user.retailer_user.retailer)

        context.update({
            'customers': customers
        })

        return context
