from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.widgets import CountrySelectWidget
from allauth.account import forms as login_form
from django.core.exceptions import ValidationError

User = get_user_model()


class UserUpdateForm(UserChangeForm):
    featured_img = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = (
                  'email',
                  'username',
                  'first_name',
                  'last_name',
                  'country',
                  'featured_img',
                  'gender',
                  )
        exclude = ['password']

    
    # def save(self, *args, **kwargs):
    #     profile = super().save(commit=False)
    #     post_save.disconnect(update_user_profile, sender=Profile)
    #     profile.save()
    #     post_save.connect(update_user_profile, sender=Profile)
        
    
class UserCreateForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields = (
					'email',
					'username',
					'first_name',
					'last_name',
					'country',
					'featured_img',
					'gender',
				)
		widgets = {'country': CountrySelectWidget()}
    
	def clean_username(self):
		username = self.cleaned_data['username']

		if ' ' in username:
			raise ValidationError("Username cannot contain spaces.")

		if len(username) < 3 or len(username) > 12:
			raise ValidationError("Username must be between 3 and 12 characters.")
			
		return username
        
class UserLoginForm(login_form.LoginForm):
    class Meta:
        def __init__(self):
            super(login_form.LoginForm, self).__init__()
            for field in self.fields:
                field.update({'class': 'form-control'})
        

class UserPasswordResetForm(forms.ModelForm):
    confirm_password = forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
    class Meta:
        model = User
        fields = ('password',)
        widgets = {'password': forms.PasswordInput(attrs={'placeholder': 'New password'})}
        
        