from django.db import models
from django.utils.html import mark_safe
from common import models as common_models
from shortuuid.django_fields import ShortUUIDField

class Category(common_models.TimeStampedUUIDModel):
	cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='cat', alphabet='abcdefgh12345')
	title = models.CharField(max_length=100, default="Category Name")
	image = models.ImageField(upload_to='category', default="category.jpg")

	class Meta:
		verbose_name_plural = 'Categories'

	def category_image(self):
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	def __str__(self):
		return self.title
