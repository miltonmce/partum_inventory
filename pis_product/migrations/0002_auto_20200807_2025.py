# Generated by Django 3.1 on 2020-08-08 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pis_product', '0001_initial'),
        ('pis_com', '0002_auto_20200807_2025'),
        ('pis_sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockout',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_invoice', to='pis_sales.saleshistory'),
        ),
        migrations.AddField(
            model_name='stockout',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockout_product', to='pis_product.product'),
        ),
        migrations.AddField(
            model_name='stockout',
            name='purchased_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_purchased', to='pis_product.purchasedproduct'),
        ),
        migrations.AddField(
            model_name='stockin',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockin_product', to='pis_product.product'),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_invoice', to='pis_sales.saleshistory'),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_product', to='pis_product.product'),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='pis_product.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_product', to='pis_com.retailer'),
        ),
        migrations.AddField(
            model_name='extraitems',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_extra_items', to='pis_com.retailer'),
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_claimed_items', to='pis_com.customer'),
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claimed_product', to='pis_product.product'),
        ),
    ]
