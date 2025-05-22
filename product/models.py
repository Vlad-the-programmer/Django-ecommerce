from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from shortuuid.django_fields import ShortUUIDField
from common import models as common_models

User = get_user_model()


RATING = (
	( 1, "★☆☆☆☆"),
	( 2, "★★☆☆☆"),
	( 3, "★★★☆☆"),
	( 4, "★★★★☆"),
	( 5, "★★★★★"),
)

def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)

class Product(common_models.TimeStampedUUIDModel):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	category = models.ForeignKey("category.Category", on_delete=models.SET_NULL, null=True, related_name="category")
	vendor = models.ForeignKey("product.Vendor", on_delete=models.SET_NULL, null=True, related_name="product")

	title = models.CharField(max_length=100, default="Product Name")
	image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
	description = RichTextUploadingField(null=True, blank=True, default="Product Description")

	price = models.DecimalField(max_digits=100, decimal_places=2, default="1.99")
	oldPrice = models.DecimalField(max_digits=100, decimal_places=2, default="2.99")

	specifications = RichTextUploadingField(null=True, blank=True)
	stockCount = models.PositiveIntegerField(default=10, null=True, blank=True)
	weight = models.CharField(max_length=100, default="0.7", null=True, blank=True)
	expirationDate = models.CharField(max_length=100, default="10", null=True, blank=True)
	tags = TaggableManager(blank=True)
	# tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

	in_stock = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	digital = models.BooleanField(default=False)

	productId = ShortUUIDField(unique=True, length=4, max_length=30, prefix="PR", alphabet='1234567890')

	class Meta:
		verbose_name_plural = 'Products'

	def product_image(self):
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	def __str__(self):
		return self.title

	def get_percentage(self):
		new_price = ((self.old_price - self.price) / self.old_price) * 100
		return new_price


class ProductImages(common_models.TimeStampedUUIDModel):
	images = models.ImageField(upload_to="product-images", default="product.jpg")
	product = models.ForeignKey(Product, related_name="p_images", on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = 'Product Images'



class ProductReview(common_models.TimeStampedUUIDModel):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='reviews')
	review = models.TextField()
	rating = models.IntegerField(choices=RATING, default=None)

	class Meta:
		verbose_name_plural = 'Reviews'

	def __str__(self):
		return self.product.title

	def get_rating(self):
		return self.rating

class Vendor(common_models.TimeStampedUUIDModel):
	name = models.CharField(max_length=100, help_text="Vendor Name", null=False, blank=False)
	image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
	description = RichTextUploadingField(null=True, blank=True, default="Vendor Description")

	address = models.CharField(max_length=100, null=False, blank=False)
	contact = models.CharField(max_length=100, null=False, blank=False)
	email = models.CharField(max_length=100,  null=False, blank=False)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = 'Vendors'

	def vendor_image(self):
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	def __str__(self):
		return self.title

