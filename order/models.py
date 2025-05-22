from django.db import models
from django.utils.html import mark_safe
from userauths.models import User
from django.utils.translation import gettext_lazy as _
from common import models as common_models

class OrderStatus(models.TextChoices):
    PENDING = "pending", _("Pending")
    SHIPPING_OUT = "shipping_out", _("Shipping Out")
    SHIPPED = "shipped", _("Shipped")
    DELIVERED = "delivered", _("Delivered")
    PAID = "paid", _("Paid")
    UNPAID = "unpaid", _("Unpaid")
    
class PaymentMethod(models.TextChoices):
    CREDIT_CARD = "credit_card", _("Credit Card")
    PAYPAL = "paypal", _("PayPal")
    BANK_TRANSFER = "bank_transfer", _("Bank Transfer")
    CASH_ON_DELIVERY = "cash_on_delivery", _("Cash on Delivery")

class DeliveryMethod(models.TextChoices):
    STANDARD = "standard", _("Standard Delivery")
    EXPRESS = "express", _("Express Delivery")
    PICKUP = "pickup", _("Store Pickup")
    
    
class Order(common_models.TimeStampedUUIDModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	orderStatus = models.CharField(choices=OrderStatus.choices, max_length=30, default=OrderStatus.PENDING)
	payment_method = models.CharField(choices=PaymentMethod.choices, max_length=30, default=PaymentMethod.CREDIT_CARD)
	delivery_method = models.CharField(choices=DeliveryMethod.choices, max_length=30, default=DeliveryMethod.STANDARD)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=1.99)
	isPaid = models.BooleanField(default=False)
	order_date = models.DateTimeField(auto_now_add=True)
	orderItems = models.ManyToManyField("product.Product", through="OrderItem")
 
	class Meta:
		verbose_name_plural = "Orders"

	def __str__(self):
		return f"Order #{self.id} - {self.user}"


class OrderItem(common_models.TimeStampedUUIDModel):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	price = models.DecimalField(max_digits=10, decimal_places=2)
 
	class Meta:
		verbose_name_plural = 'Order Items'

	def order_img(self):
		return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image))

	def __str__(self):
		return f"{self.product.title} x {self.quantity} - Order #{self.order.id}"


