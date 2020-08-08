from __future__ import unicode_literals
from django.contrib import admin

from pis_com.models import UserProfile, Employee, EmployeeSalary
from pis_com.models import Customer, FeedBack
from pis_com.models import AdminConfiguration
from pis_com.models import ExtraExpense
from pis_com.models import Ledger
from pis_com.models.retailer import Retailer
from pis_com.models.retaileruser import RetailerUser
from pis_com.models.supplier import Supplier
from pis_com.models.supplierstatement import SupplierStatement


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'first_name', 'last_name', 'phone_no',
        'email', 'user_type'
    )
    search_fields = (
        'user__username', 'user__first_name', 'user__last_name',
        'user__email', 'phone_no'
    )

    @staticmethod
    def first_name(obj):
        return obj.user.first_name

    @staticmethod
    def last_name(obj):
        return obj.user.last_name

    @staticmethod
    def email(obj):
        return obj.user.email


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'customer_phone','customer_type', 'retailer'
    )

class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer','description','date'
    )
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(FeedBack, FeedbackAdmin)
admin.site.register(AdminConfiguration)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'name', 'father_name', 'mobile', 'address','date_of_joining'
    )
    search_fields = (
        'name', 'cnic',
    )

    @staticmethod
    def name(obj):
        return obj.name


class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'employee' ,'salary_amount', 'date'
    )

    @staticmethod
    def employee(obj):
        return obj.employee.name
    search_fields = (
         'date',
    )



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)

class ExtraExpenseAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'amount', 'description', 'date'
    )
    search_fields = (
        'amount', 'description',
    )

    @staticmethod
    def amount(obj):
        return obj.amount

admin.site.register(ExtraExpense, ExtraExpenseAdmin)




class LedgerAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer','invoice','person', 'amount','payment',
        'description','dated', 'created_at'
    )
    search_fields = (
        'customer__customer_name', 'customer__customer_phone',
        'customer__person_type','customer__retailer__name'
    )
    raw_id_fields = ('customer',)

    @staticmethod
    def retailer(obj):
        return obj.retailer.name


admin.site.register(Ledger, LedgerAdmin)

admin.site.register(Supplier)
admin.site.register(SupplierStatement)

class RetailerAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'slug', 'created_at', 'updated_at',
        'package', 'package_price', 'package_expiry'
    )
    search_fields = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


class RetailerUserAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer', 'employee_name', 'email', 'phone_no', 'mobile_no',)
    search_fields = (
        'user__username', 'user__first_name', 'user__last_name',
        'user__email', 'user__user_profile__phone_no',
        'user__user_profile__mobile_no', 'retailer__name'
    )
    raw_id_fields = ('retailer', 'user')

    @staticmethod
    def retailer(obj):
        return obj.retailer.name

    @staticmethod
    def email(obj):
        return obj.user.email

    @staticmethod
    def phone_no(obj):
        return obj.user.user_profile.phone_no

    @staticmethod
    def employee_name(obj):
        return '%s %s' % (obj.user.first_name, obj.user.last_name)

    @staticmethod
    def mobile_no(obj):
        return obj.user.user_profile.mobile_no


admin.site.register(Retailer, RetailerAdmin)
admin.site.register(RetailerUser, RetailerUserAdmin)