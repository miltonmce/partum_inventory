from django import forms

from pis_com.models.supplierstatement import SupplierStatement


class SupplierStatementForm(forms.ModelForm):
    class Meta:
        model = SupplierStatement
        fields = '__all__'