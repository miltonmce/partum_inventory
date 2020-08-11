from django import forms

from pis_com.models import ProductDetail


class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetail
        fields = "__all__"