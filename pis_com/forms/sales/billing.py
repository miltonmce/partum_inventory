from django import forms

from pis_com.models.saleshistory import SalesHistory


class BillingForm(forms.ModelForm):
    class Meta:
        model = SalesHistory
        fields = "__all__"