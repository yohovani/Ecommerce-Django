from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.
class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status','is_ordered','created_at']
    list_filter = ['status','is_ordered']
    search_filter = ['order_number','first_name','last_name','phone','email'] 
    list_perf_page = 20
    inlines = [OrderProductInLine]

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)