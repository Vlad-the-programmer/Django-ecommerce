from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Wishlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey("core.Product", on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = 'Wishlists'

	def __str__(self):
		return self.product.title
