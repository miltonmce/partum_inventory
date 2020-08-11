from django.urls import reverse_lazy
from django.views.generic import DeleteView

from pis_com.models import PurchasedProduct, StockOut, Ledger
from pis_com.models.saleshistory import SalesHistory


class SalesDeleteView(DeleteView):
    model = SalesHistory
    success_url = reverse_lazy('invoice_list')

    def get(self, request, *args, **kwargs):
        PurchasedProduct.objects.filter(
            invoice__id=self.kwargs.get('pk')).delete()
        StockOut.objects.filter(
            invoice__id=self.kwargs.get('pk')).delete()
        Ledger.objects.filter(
            invoice__id=self.kwargs.get('pk')).delete()
        return self.delete(request, *args, **kwargs)
