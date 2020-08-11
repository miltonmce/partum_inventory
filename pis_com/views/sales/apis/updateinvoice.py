import json

from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from pis_com.forms.product.stockout import StockOutForm
from pis_com.models import PurchasedProduct, StockOut, Customer, Ledger
from pis_com.models.saleshistory import SalesHistory


class UpdateInvoiceAPIView(View):

    def __init__(self, *args, **kwargs):
        super(UpdateInvoiceAPIView, self).__init__(*args, **kwargs)
        self.customer = None
        self.invoice = None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            UpdateInvoiceAPIView, self).dispatch(request, *args, **kwargs)

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
        invoice_id = self.request.POST.get('invoice_id')
        items = json.loads(self.request.POST.get('items'))
        purchased_items_id = []
        extra_items_id = []

        with transaction.atomic():
            for item in items:

                if item.get('item_id'):
                    # Getting Purchased Item by using Item ID or Invoice ID
                    # We are getting that by using Item ID
                    purchased_item = PurchasedProduct.objects.get(
                        id=item.get('item_id'),
                    )

                    # Delete the previous Stock Out Object,
                    # We need to create new one if quantity would not be same

                    if not purchased_item.quantity == item.get('qty'):
                        StockOut.objects.filter(
                            invoice__id=invoice_id,
                            stock_out_quantity='%g' % purchased_item.quantity,
                        ).delete()

                        # Update Purchased Product Details
                        purchased_item.price = item.get('price')
                        purchased_item.quantity = item.get('qty')
                        purchased_item.discount_percentage = item.get('perdiscount')
                        purchased_item.purchase_amount = item.get('total')
                        purchased_item.save()
                        purchased_items_id.append(purchased_item.id)

                        # Creating New stock iif quantity would get changed
                        stock_out_form_kwargs = {
                            'invoice': invoice_id,
                            'product': purchased_item.product.id,
                            'purchased_item': purchased_item.id,
                            'stock_out_quantity': item.get('qty'),
                            'dated': timezone.now().date()
                        }

                        stock_out_form = StockOutForm(stock_out_form_kwargs)
                        if stock_out_form.is_valid():
                            stock_out_form.save()

            invoice = SalesHistory.objects.get(id=invoice_id)
            invoice.discount = discount
            invoice.grand_total = grand_total
            invoice.total_quantity = totalQty
            invoice.shipping = shipping
            invoice.purchased_items = purchased_items_id
            invoice.extra_items = extra_items_id
            invoice.paid_amount = paid_amount
            invoice.remaining_payment = remaining_payment
            invoice.retailer = self.request.user.retailer_user.retailer

            if self.request.POST.get('customer_id'):
                invoice.customer = Customer.objects.get(
                    id=self.request.POST.get('customer_id'))

            invoice.save()

            if invoice.customer:
                ledger = Ledger.objects.get(
                    customer__id=invoice.customer.id,
                    invoice__id=invoice.id
                )
                ledger.amount = remaining_payment
                ledger.save()

        return JsonResponse({'invoice_id': invoice.id})
