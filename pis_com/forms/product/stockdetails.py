from django import forms

from pis_com.models import StockIn


class StockDetailsForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = "__all__"
