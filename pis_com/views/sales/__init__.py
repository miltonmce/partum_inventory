from django.urls import re_path

from pis_com.views.sales.apis.generateinvoice import GenerateInvoiceAPIView
from pis_com.views.sales.apis.productdetail import ProductDetailsAPIView
from pis_com.views.sales.apis.productitem import ProductItemAPIView
from pis_com.views.sales.apis.updateinvoice import UpdateInvoiceAPIView
from pis_com.views.sales.createinvoice import CreateInvoiceView
from pis_com.views.sales.invoicedetail import InvoiceDetailView
from pis_com.views.sales.invoiceslist import InvoicesList
from pis_com.views.sales.salesdelete import SalesDeleteView
from pis_com.views.sales.updateinvoice import UpdateInvoiceView

urlpatterns = [
    re_path(r'^sales/create/invoice/$',CreateInvoiceView.as_view(),name='create_invoice'),
    re_path(r'^sales/update/(?P<id>\d+)/api/$',UpdateInvoiceView.as_view(),name='invoice_update'),
    re_path(r'^sales/product/items/details/$',ProductItemAPIView.as_view(),name='product_item_api'),
    re_path(r'^sales/invoice/list/$',InvoicesList.as_view(),name='invoice_list'),
    re_path(r'^sales/api/generate/invoice/$',GenerateInvoiceAPIView.as_view(),name='generate_invoice_api'),
    re_path(r'^sales/api/update/invoice/$',UpdateInvoiceAPIView.as_view(),name='update_invoice_api'),
    re_path(r'^sales/invoice/(?P<invoice_id>\d+)/detail/$',InvoiceDetailView.as_view(),name='invoice_detail'),
    re_path(r'^sales/api/product/details/$',ProductDetailsAPIView.as_view(),name='product_details_api'),
    re_path(r'^sales/invoice/(?P<pk>\d+)/delete/$',SalesDeleteView.as_view(),name='delete'),
]