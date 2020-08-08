from django import forms

from pis_com.models.retailer import Retailer


class RetailerForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Retailer