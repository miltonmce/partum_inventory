from django.urls import re_path

from pis_com.views.product.claimeditems_list import ClaimedItemsListView
from pis_com.views.product.claimedproduct_form import ClaimedProductFormView
from pis_com.views.product.extraitems import ExtraItemsView
from pis_com.views.product.logs.dailystock import DailyStockLogs
from pis_com.views.product.logs.monthlystock import MonthlyStockLogs
from pis_com.views.product.newproduct import AddNewProduct
from pis_com.views.product.newproduct_items import AddProductItems
from pis_com.views.product.newstockitems import AddStockItems
from pis_com.views.product.productdetail_list import ProductDetailList
from pis_com.views.product.productlist import ProductItemList
from pis_com.views.product.productupdate import ProductUpdateView
from pis_com.views.product.purchaseditems import PurchasedItems
from pis_com.views.product.stockdetail import StockDetailView
from pis_com.views.product.stockin_list import StockInListView
from pis_com.views.product.stockinupdate import StockInUpdateView
from pis_com.views.product.stockitem_list import StockItemList
from pis_com.views.product.stockout_items import StockOutItems
from pis_com.views.product.stockout_list import StockOutListView

urlpatterns = [
    re_path(r'^product/items/list/$', ProductItemList.as_view(), name='items_list'),
    re_path(r'^product/item/(?P<pk>\d+)/detail/list/$',ProductDetailList.as_view(),name='item_details'),
    re_path(r'^product/retailer/(?P<retailer_id>\d+)/add/$',AddNewProduct.as_view(),name='add_product'),
    re_path(r'^product/item/(?P<product_id>\d+)/add/$',AddProductItems.as_view(),name='add_product_items'),
    re_path(r'^product/items/purchased/$', PurchasedItems.as_view(),name='purchased_items'),
    re_path(r'^product/items/extra/purchased/$', ExtraItemsView.as_view(),name='purchased_extra_items'),
    re_path(r'^product/items/claimed/$', ClaimedProductFormView.as_view(),name='claimed_items'),
    re_path(r'^product/items/claimed/list/$', ClaimedItemsListView.as_view(),name='claimed_items_list'),
    re_path(r'^product/stock/items/list/$', StockItemList.as_view(), name='stock_items_list'),
    re_path(r'^product/stock/item/(?P<product_id>\d+)/add/$',AddStockItems.as_view(),name='add_stock_items'),
    re_path(r'^product/stock/item/(?P<product_id>\d+)/out/$',StockOutItems.as_view(),name='stock_out_items'),
    re_path(r'^product/stock/item/(?P<product_id>\d+)/detail/$',StockDetailView.as_view(),name='stock_detail'),
    re_path(r'^product/(?P<product_id>\d+)/stock/in/$',StockInListView.as_view(),name='stockin_list'),
    re_path(r'^product/(?P<product_id>\d+)/stock/out/$',StockOutListView.as_view(),name='stockout_list'),
    re_path(r'^product/(?P<pk>\d+)/update/$',ProductUpdateView.as_view(),name='update_product'),
    re_path(r'^product/(?P<pk>\d+)/stockin/update/$',StockInUpdateView.as_view(),name='update_stockin'),

    # Logs
    re_path(r'^stock/logs/daily/$', DailyStockLogs.as_view(),name='daily_stock_logs'),
    re_path(r'^stock/logs/monthly/$', MonthlyStockLogs.as_view(),name='monthly_stock_logs'),
]
