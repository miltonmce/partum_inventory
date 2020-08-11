from django import forms

from pis_com.models import StockOut


class StockOutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = "__all__"