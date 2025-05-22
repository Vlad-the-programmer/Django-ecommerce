from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from shortuuid.django_fields import ShortUUIDField
from common import models as common_models
import uuid

User = get_user_model()


class PostStatus(models.TextChoices):
	DRAFT = "draft", _("Draft"),
	DISABLED= "disabled", _("Disabled"),
	REJECTED = "rejected", _("Rejected"),
	IN_REVIEW = "in_review", _("In Review"),
	PUBLISHED = "published", _("Published"),
    
    
class PostCategory(common_models.TimeStampedUUIDModel):
	cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='cat', alphabet='abcdefgh12345')
	title = models.CharField(max_length=100, default="Category Name")

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title

class Post(common_models.TimeStampedUUIDModel):
	id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	categories = models.ManyToManyField(PostCategory, related_name="categories")

	tags = TaggableManager(blank=True)

	image = models.ImageField(upload_to='blog', default="blog.jpg")
	title = models.CharField(max_length=100, default="Post Name")
	subtitle = models.TextField(null=True, blank=True, default="Post Subtitle")
	
	body = RichTextUploadingField(null=True, blank=True, default="Post Body")

	post_status = models.CharField(choices=PostStatus, max_length=10, default=PostStatus.IN_REVIEW)

	class Meta:
		verbose_name_plural = 'Posts'

	def blog_image(self):
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	def __str__(self):
		return self.title

class Comment(common_models.TimeStampedUUIDModel):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	body = models.TextField()

	class Meta:
		verbose_name_plural = 'Comments'

	def __str__(self):
		return self.post.title

