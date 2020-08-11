from __future__ import unicode_literals
from django.contrib import admin

from pis_com.models import UserProfile, Employee, EmployeeSalary, Product, ProductDetail, PurchasedProduct, ExtraItems, \
    ClaimedProduct, StockIn, StockOut
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



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'brand_name','UNIT_TYPE_QUANTITY', 'retailer',
        'quantity', 'retail_price', 'consumer_price','bar_code'
    )
    search_fields = (
        'name', 'brand_name', 'retailer__name','bar_code','unit_type'
    )
    raw_id_fields = ('retailer',)

    @staticmethod
    def retailer(obj):
        return obj.retailer.name

    @staticmethod
    def quantity(obj):
        return 'under progress'

    @staticmethod
    def retail_price(obj):
        return 'under progress'

    @staticmethod
    def consumer_price(obj):
        return 'under progress'


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'brand_name', 'retailer', 'retail_price',
        'consumer_price', 'discount_amount', 'profit_amount',
        'available_item', 'purchased_item', 'remaining_item'
    )

    search_fields = (
        'product__name', 'product__retailer__name', 'product__brand_name'
    )

    raw_id_fields = ('product',)

    @staticmethod
    def retailer(obj):
        return obj.product.retailer.name

    @staticmethod
    def brand_name(obj):
        return obj.product.brand_name

    @staticmethod
    def discount_amount(obj):
        return 'under_progress'

    @staticmethod
    def profit_amount(obj):
        return obj.consumer_price - obj.retail_price

    @staticmethod
    def remaining_item(obj):
        return obj.available_item - obj.purchased_item


class PurchasedProductAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer', 'invoice_no', 'discount_percentage', 'created_at'
    )

    search_fields = ('product__name', 'product__retailer__name')
    raw_id_fields = ('product',)

    @staticmethod
    def retailer(obj):
        return obj.product.retailer.name

    @staticmethod
    def invoice_no(obj):
        return obj.invoice.receipt_no if obj.invoice else ''


class ExtraItemsAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'retailer', 'quantity', 'price', 'discount_percentage',
        'total')

    search_fields = ('item_name', 'retailer__name')
    raw_id_fields = ('retailer', )

    @staticmethod
    def retailer(obj):
        return obj.product.retailer.item_name


class ClaimedProductAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'brand_name', 'customer', 'claimed_items',
        'claimed_amount', 'created_at'
    )
    search_fields = ('product__name', 'product__brand_name')
    raw_id_fields = ('product',)

    @staticmethod
    def brand_name(obj):
        return obj.product.brand_name or None

    @staticmethod
    def customer(obj):
        return obj.customer.customer_name or None


class StockInAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'product', 'quantity', 'price_per_item',
        'total_amount', 'dated_order','stock_expiry'
    )
    search_fields = ('product__name','stock_expiry','dated_order')


class StockOutAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'product', 'invoice_no', 'stock_out_quantity', 'dated',
    )
    search_fields = ('product__name','stock_out_quantity','dated')

    @staticmethod
    def invoice_no(obj):
        return obj.invoice.receipt_no if obj.invoice else ''


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(PurchasedProduct, PurchasedProductAdmin)
admin.site.register(ExtraItems, ExtraItemsAdmin)
admin.site.register(ClaimedProduct, ClaimedProductAdmin)
admin.site.register(StockIn, StockInAdmin)
admin.site.register(StockOut, StockOutAdmin)