import json

from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from pis_com.forms.customer.customer import CustomerForm
from pis_com.forms.ledger.ledger import LedgerForm
from pis_com.forms.product.extraitem import ExtraItemForm
from pis_com.forms.product.purchasedproduct import PurchasedProductForm
from pis_com.forms.product.stockout import StockOutForm
from pis_com.forms.sales.billing import BillingForm
from pis_com.models import Product


class GenerateInvoiceAPIView(View):

    def __init__(self, *args, **kwargs):
        super(GenerateInvoiceAPIView, self).__init__(*args, **kwargs)
        self.customer = None
        self.invoice = None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            GenerateInvoiceAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        customer_name = self.request.POST.get('customer_name')
        customer_phone = self.request.POST.get('customer_phone')
        sub_total = self.request.POST.get('sub_total')
        discount = self.request.POST.get('discount')
        shipping = self.request.POST.get('shipping')
        grand_total = self.request.POST.get('grand_total')
        totalQty = self.request.POST.get('totalQty')
        remaining_payment = self.request.POST.get('remaining_amount')
        paid_amount = self.request.POST.get('paid_amount')
        cash_payment = self.request.POST.get('cash_payment')
        returned_cash = self.request.POST.get('returned_cash')
        items = json.loads(self.request.POST.get('items'))
        purchased_items_id = []
        extra_items_id = []

        with transaction.atomic():

            billing_form_kwargs = {
                'discount': discount,
                'grand_total': grand_total,
                'total_quantity': totalQty,
                'shipping': shipping,
                'paid_amount': paid_amount,
                'remaining_payment': remaining_payment,
                'cash_payment': cash_payment,
                'returned_payment': returned_cash,
                'retailer': self.request.user.retailer_user.retailer.id,
            }

            if self.request.POST.get('customer_id'):
                billing_form_kwargs.update({
                    'customer': self.request.POST.get('customer_id')
                })
            else:
                customer_form_kwargs = {
                    'customer_name': customer_name,
                    'customer_phone': customer_phone,
                    'retailer': self.request.user.retailer_user.retailer.id
                }
                customer_form = CustomerForm(customer_form_kwargs)
                if customer_form.is_valid():
                    self.customer = customer_form.save()
                    billing_form_kwargs.update({
                        'customer': self.customer.id
                    })

            billing_form = BillingForm(billing_form_kwargs)
            self.invoice = billing_form.save()

            for item in items:
                item_name = item.get('item_name')
                try:
                    product = Product.objects.get(
                        name=item_name,
                        retailer=self.request.user.retailer_user.retailer
                    )
                    form_kwargs = {
                        'product': product.id,
                        'invoice': self.invoice.id,
                        'quantity': item.get('qty'),
                        'price': item.get('price'),
                        'discount_percentage': item.get('perdiscount'),
                        'purchase_amount': item.get('total'),
                    }
                    form = PurchasedProductForm(form_kwargs)
                    if form.is_valid():
                        purchased_item = form.save()
                        purchased_items_id.append(purchased_item.id)

                        latest_stock_in = (
                            product.stockin_product.all().latest('id'))

                        stock_out_form_kwargs = {
                            'product': product.id,
                            'invoice': self.invoice.id,
                            'purchased_item': purchased_item.id,
                            'stock_out_quantity': float(item.get('qty')),
                            'buying_price': (
                                float(latest_stock_in.buying_price_item) *
                                float(item.get('qty'))),
                            'selling_price': (
                                float(item.get('price')) * float(item.get('qty'))),
                            'dated': timezone.now().date()
                        }

                        stock_out_form = StockOutForm(stock_out_form_kwargs)
                        if stock_out_form.is_valid():
                            stock_out = stock_out_form.save()

                except Product.DoesNotExist:
                    extra_item_kwargs = {
                        'retailer': self.request.user.retailer_user.retailer.id,
                        'item_name': item.get('item_name'),
                        'quantity': item.get('qty'),
                        'price': item.get('price'),
                        'discount_percentage': item.get('perdiscount'),
                        'total': item.get('total'),
                    }
                    extra_item_form = ExtraItemForm(extra_item_kwargs)
                    if extra_item_form.is_valid():
                        extra_item = extra_item_form.save()
                        extra_items_id.append(extra_item.id)

            self.invoice.purchased_items = purchased_items_id
            self.invoice.extra_items = extra_items_id
            self.invoice.save()

            if self.customer or self.request.POST.get('customer_id'):
                if float(remaining_payment):
                    ledger_form_kwargs = {
                        'retailer': self.request.user.retailer_user.retailer.id,
                        'customer': (
                            self.request.POST.get('customer_id') or
                            self.customer.id),
                        'invoice': self.invoice.id,
                        'amount': remaining_payment,
                        'description': (
                            'Remaining Payment for Bill/Receipt No %s '
                            % self.invoice.receipt_no),
                        'dated': timezone.now()
                    }

                    ledgerform = LedgerForm(ledger_form_kwargs)
                    if ledgerform.is_valid():
                        ledger = ledgerform.save()

            return JsonResponse({'invoice_id': self.invoice.id})
