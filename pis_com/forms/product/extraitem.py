from django import forms

from pis_com.models import ExtraItems


class ExtraItemForm(forms.ModelForm):
    class Meta:
        model = ExtraItems
        fields = "__all__"