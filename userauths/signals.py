from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# AllAuth
from allauth.account.signals import user_signed_up, email_confirmed
from .emails_handler import send_verification_email

User = get_user_model()


@receiver(post_save, sender=User)
def save_user_profile(sender, created, instance, *args, **kwargs):
    profile = instance
    if created and profile:
        if not profile.username:
            profile.username = profile.set_username()

        profile.save()
                  
            
@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    user.is_active = False
    print('u', user)
    user.save()
    
    # send_confirmation_email.delay(request, user)
    
    # Sending email activation
    mail_subject = 'Please activate your account'
    template_email = 'accounts/account_verification_email.html'
    send_verification_email.delay(request,
                            user,
                            template_email,
                            mail_subject,
                            is_activation_email=True)
    messages.add_message(
        request, 
        messages.INFO,
        message=f"Confirmation email has been sent to {user.email}",
    )
     
     
# @receiver(email_confirmed)
# def email_confirmed_(request, email_address, *args, **kwargs):
#     user = User.objects.get(
#         email=email_address.email)
#     user.is_active = True
#     user.save()
    
    
# @receiver(post_save, sender=User)
# def update_user_profile(sender, created, instance, *args, **kwargs):
#     profile = instance
#     if not created and profile:
#         print("Worked")
#         profile.save()