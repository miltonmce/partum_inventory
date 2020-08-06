# Generated by Django 3.1 on 2020-08-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis_sales', '0011_auto_20200804_2039'),
        ('pis_retailer', '0006_retailer_package_expiry'),
        ('pis_com', '0014_extraexpense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person', models.CharField(blank=True, default='customer', max_length=200, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('dated', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_ledger', to='pis_com.customer')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledger_invoice', to='pis_sales.saleshistory')),
                ('retailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retailer_ledger', to='pis_retailer.retailer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
