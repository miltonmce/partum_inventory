from django.urls import re_path


from .newexpense import AddNewExpense
from .listview import ExpenseListView
from .dashboard import dashboard
from .deleteexpense import ExpenseDelete


urlpatterns = [
    re_path(r'^add/new/expense/$', AddNewExpense.as_view(), name='add_new_expense'),
    re_path(r'^list/expense$', ExpenseListView.as_view(),name='expense_list'),
    re_path(r'^dashboard/$', dashboard.as_view(),name='dashboard'),
    re_path(r'delete/expense/(?P<pk>\d+)/$',ExpenseDelete.as_view(),name='delete_expense'),
]
