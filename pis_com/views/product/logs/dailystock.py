from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from pis_com.models import StockOut


class DailyStockLogs(ListView):
    model = StockOut
    template_name = 'logs/daily_stock_logs.html'
    paginate_by = 200
    is_paginated = True

    def __init__(self, *args, **kwargs):
        super(DailyStockLogs, self).__init__(*args, **kwargs)
        self.logs_date = ''
        self.today_date = ''

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(
            DailyStockLogs, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.logs_date = self.request.GET.get('date')
        if self.logs_date:
            logs_date = self.logs_date.split('-')
            year = logs_date[0]
            month = logs_date[1]
            day = logs_date[2]

            try:
                queryset = StockOut.objects.filter(
                    dated__year=year,
                    dated__month=month,
                    dated__day=day,
                ).values('product__name').annotate(
                    receipt_item=Count('product__name'),
                    total_qty=Sum('stock_out_quantity')
                )
            except:
                queryset = []
        else:
            self.today_date = timezone.now().date()
            queryset = StockOut.objects.filter(
                dated__year=self.today_date.year,
                dated__month=self.today_date.month,
                dated__day=self.today_date.day,
            ).values('product__name').annotate(
                receipt_item=Count('product__name'),
                total_qty=Sum('stock_out_quantity')
            )

        return queryset.order_by('product__name')

    def get_context_data(self, **kwargs):
        context = super(DailyStockLogs, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        if queryset:
            total = queryset.aggregate(Sum('selling_price'))
            total = total.get('selling_price__sum') or 0
        else:
            total = 0

        context.update({
            'total': total,
            'today_date': (
                timezone.now().strftime('%Y-%m-%d')
                if self.today_date else None),
            'logs_date': self.logs_date,
        })
        return context
