from django.db import models
from django.contrib.auth import get_user_model
from common import models as common_models

User = get_user_model()


class ContactUs(common_models.TimeStampedUUIDModel):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField()

	class Meta:
		verbose_name = 'Contact Us'
		verbose_name_plural = 'Contact Us'

	def __str__(self):
		return self.name
