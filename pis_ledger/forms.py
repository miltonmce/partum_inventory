from django import forms

from pis_com.models import Ledger


class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = "__all__"

