from django import forms

from pis_com.models import PurchasedProduct


class PurchasedProductForm(forms.ModelForm):
    class Meta:
        model = PurchasedProduct
        fields = "__all__"