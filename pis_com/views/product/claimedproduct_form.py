from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from pis_com.forms.product.claimedproduct import ClaimedProductForm


class ClaimedProductFormView(FormView):
    template_name = 'products/claimed_product.html'
    form_class = ClaimedProductForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            ClaimedProductFormView, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def purchased_items_update(claimed_item, claimed_number):
        product = (
            claimed_item.product.product_detail.filter(
                available_item__gte=claimed_number
            ).first()
        )
        product.purchased_item = (
                product.purchased_item - claimed_number
        )
        product.save()

    # def claimed_items_payment(self, claimed_item, amount):
    #     payment_form_kwargs = {
    #         'customer': claimed_item.customer.id,
    #         'retailer': self.request.user.retailer_user.retailer.id,
    #         'amount': amount,
    #         'description': 'Amount Refunded from Claimed'
    #                        ' Item ID (%s)' % claimed_item.id
    #     }
    #     payment_form = PaymentForm(payment_form_kwargs)
    #     if payment_form.is_valid():
    #         payment_form.save()

    def form_valid(self, form):
        claimed_item = form.save()

        # update the purchased product accordingly
        self.purchased_items_update(
            claimed_item=claimed_item,
            claimed_number=int(form.cleaned_data.get('claimed_items'))
        )

        # Doing a payment of claimed amount
        # self.claimed_items_payment(
        #     claimed_item=claimed_item,
        #     amount=form.cleaned_data.get('claimed_amount')
        # )

        return HttpResponseRedirect(reverse('items_list'))

    def form_invalid(self, form):
        return super(ClaimedProductFormView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(
            ClaimedProductFormView, self).get_context_data(**kwargs)

        products = (
            self.request.user.retailer_user.retailer.
                retailer_product.all().order_by('name')
        )
        customers = (
            self.request.user.retailer_user.retailer.
                retailer_customer.all().order_by('customer_name')
        )
        context.update({
            'products': products,
            'customers': customers,
        })

        return context
