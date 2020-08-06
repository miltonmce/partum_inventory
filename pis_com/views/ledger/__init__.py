from django.urls import re_path

from pis_com.views.ledger.customerledger import CustomerLedgerView
from pis_com.views.ledger.newledger import AddNewLedger
from pis_com.views.ledger.newcustomer_ledger import AddLedger
from pis_com.views.ledger.customerledger_detail import CustomerLedgerDetailsView
from pis_com.views.ledger.addpayment import AddPayment

urlpatterns = [
    re_path(r'^ledger/add/new/$', AddNewLedger.as_view(), name='add_new_ledger'),
    re_path(r'^ledger/list/customer/$', CustomerLedgerView.as_view(),name='customer_ledger_list'),
    re_path(r'^ledger/add/customer/(?P<customer_id>\d+)/ledger/$',AddLedger.as_view(),name='add_ledger'),
    re_path(r'^ledger/add/customer/(?P<customer_id>\d+)/payment/$',AddPayment.as_view(),name='add_payment'),
    re_path(r'^ledger/customer/(?P<customer_id>\d+)/ledger/details/$',CustomerLedgerDetailsView.as_view(),name='customer_ledger_detail'),
]
