from django import forms

from pis_com.models.retaileruser import RetailerUser


class RetailerUserForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = RetailerUser