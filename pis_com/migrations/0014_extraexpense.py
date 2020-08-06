# Generated by Django 3.1 on 2020-08-06 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_com', '0013_employee_employeesalary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]