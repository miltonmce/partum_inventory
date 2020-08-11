from django import forms

from pis_com.models import ClaimedProduct


class ClaimedProductForm(forms.ModelForm):
    class Meta:
        model = ClaimedProduct
        fields = "__all__"