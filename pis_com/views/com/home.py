from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.db.models import Sum
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        a = self.request
        print(a)

        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:

            if self.request.user.retailer_user:
                if (
                    self.request.user.retailer_user.role_type ==
                        self.request.user.retailer_user.ROLE_TYPE_SALESMAN
                ):
                    return HttpResponseRedirect(reverse('sales:invoice_list'))
            if self.request.user.retailer_user:
                if (
                        self.request.user.retailer_user.role_type ==
                        self.request.user.retailer_user.ROLE_TYPE_DATA_ENTRY_USER
                ):
                    return HttpResponseRedirect(reverse('product:items_list'))

        return super(
            HomePageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        sales = self.request.user.retailer_user.retailer.retailer_sales.all()
        sales_sum = sales.aggregate(
            total_sales=Sum('grand_total')
        )

        today_sales = (
            self.request.user.retailer_user.retailer.
            retailer_sales.filter(
                created_at__icontains=timezone.now().date()
            )
        )
        today_sales_sum = today_sales.aggregate(
            total_sales=Sum('grand_total')
        )

        context.update({
            'sales_count': sales.count(),
            'sales_sum': (
                int(sales_sum.get('total_sales')) if
                sales_sum.get('total_sales') else 0
            ),
            'today_sales_count': today_sales.count(),
            'today_sales_sum': (
                int(today_sales_sum.get('total_sales')) if
                today_sales_sum.get('total_sales') else 0
            )
        })

        return context
