from django.db import models
from django.shortcuts import get_object_or_404
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.utils.html import mark_safe

class Gender(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    OTHER = "other", _("Other")
    
class User(AbstractUser):
	email = models.EmailField(unique=True, 
                              blank=True,
                              null=True, 
                              max_length=254,
                              validators=[
                                            validators.EmailValidator()
                                        ])
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	gender = models.CharField(_('Gender'),
                              max_length=10,
                              choices=Gender.choices,
                              default=_('Male'),
                              null=True)
	country = CountryField(blank_label=_('(select country)'),
	                       default='',
	                       max_length=50,
	                    )
	featured_img = models.ImageField(verbose_name=_('A profile image'),
	                                 upload_to='account-images', 
	                                 default='user.jpg')
	password = models.CharField(max_length=100, blank=True, null=True)
	username = models.CharField(unique=True, max_length=100, blank=True, null=True)
	date_joined = models.DateTimeField(auto_now_add=True, null=True)
	last_login = models.DateTimeField(_('Last logged in'), null=True, blank=True)
	is_staff = models.BooleanField(default=False, blank=True, null=True)
	is_active = models.BooleanField(default=False, blank=True, null=True)
	is_superuser = models.BooleanField(default=False, blank=True, null=True)


	def __str__(self):
		return self.email
	
	def set_username(self):
		return self.email.split('@')[0].lower()


	def has_perm(self, perm, obj=None):
		return self.is_superuser


	def has_add_permission(request):
		if request.user.is_staff:
			return True
		return False


	def has_change_permission(request):
		if request.user.is_staff:
			return True
		return False


	def has_delete_permission(request):
		if request.user.is_staff:
			return True
		return False


	def has_module_perms(self, app_label):
		return True


	@classmethod
	def get_user_by_email(cls, email):
		try:
			user = get_object_or_404(cls.__class__, email__exact=email)
		except:
			user = None
		if user is not None:
			return True
		return False 


	@property
	def get_full_name(self):
		return f"{self.first_name} {self.last_name}"

	@property
	def imageURL(self):
		try:
			url = self.featured_img.url
		except:
			url = ''
		return url
    
	@property
	def user_image(self):		
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	class Meta:
		verbose_name_plural = "Users"
		ordering = ['email']



