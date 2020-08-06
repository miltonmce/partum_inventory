from django import forms

from pis_com.models import ExtraExpense


class ExtraExpenseForm(forms.ModelForm):
    class Meta:
        model = ExtraExpense
        fields = '__all__'