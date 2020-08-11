from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from pis_com.models import StockOut


class MonthlyStockLogs(ListView):
    model = StockOut
    template_name = 'logs/monthly_stock_logs.html'
    paginate_by = 200
    is_paginated = True

    def __init__(self, *args, **kwargs):
        super(MonthlyStockLogs, self).__init__(*args, **kwargs)
        self.logs_month = ''
        self.current_month = ''
        self.year = ''

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(
            MonthlyStockLogs, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.logs_month = self.request.GET.get('month')
        current_date = timezone.now().date()
        months = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]

        if self.logs_month:
            self.year = current_date.year
            month = self.logs_month

            if month < months.index(self.logs_month) + 1:
                self.year = self.year - 1

            queryset = StockOut.objects.filter(
                dated__year=self.year,
                dated__month=months.index(self.logs_month) + 1,
            ).values('product__name').annotate(
                receipt_item=Count('product__name'),
                total_qty=Sum('stock_out_quantity')
            )

        else:
            self.current_month = months[current_date.month - 1]
            self.year = current_date.year
            queryset = StockOut.objects.filter(
                dated__year=current_date.year,
                dated__month=current_date.month,
            ).values('product__name').annotate(
                receipt_item=Count('product__name'),
                total_qty=Sum('stock_out_quantity')
            )

        return queryset.order_by('product__name')

    def get_context_data(self, **kwargs):
        context = super(MonthlyStockLogs, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        if queryset:
            total = queryset.aggregate(Sum('selling_price'))
            total = total.get('selling_price__sum') or 0
        else:
            total = 0

        context.update({
            'total': total,
            'month': self.logs_month or self.current_month,
            'year': self.year
        })
        return context
