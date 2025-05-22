from django.db import models
from django.contrib.auth import get_user_model
from common import models as common_models

User = get_user_model()

class Wishlist(common_models.TimeStampedUUIDModel):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey("product.Product", on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = 'Wishlists'

	def __str__(self):
		return self.product.title
