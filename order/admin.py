from django.contrib import admin
from order.models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
	model = Order
	list_display = ['user', 'total_price', 'isPaid', 'order_date', 'orderStatus']

class OrderItemsAdmin(admin.ModelAdmin):
	model = OrderItem
	list_display = ['order', 'product', 'quantity', 'price']
 

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemsAdmin)