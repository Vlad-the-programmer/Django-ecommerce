from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings
# Verification email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib import messages

# AllAuth
from allauth.account.models import EmailAddress, EmailConfirmation
from celery import shared_task

@shared_task
def send_verification_email(request, user, template_email,
                            mail_subject=None, is_activation_email=False):
    
    uuid = urlsafe_base64_encode(force_bytes(user.id))
    token = default_token_generator.make_token(user)
    current_site = get_current_site(request)
    message = render_to_string(template_email, {
        'user': user,
        'domain': current_site,
        'uid': uuid,
        'token': token,
    })
    to_email = user.email
    
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()
    
    if is_activation_email:
        messages.success(request, f'Thank you. We have sent you a verification email to your email address {to_email}. Please verify it.')
        return redirect('/accounts/login/?command=verification&email='+to_email)
    else:
        messages.success(request, f'Thank you. We have sent you an email with the instructions to your email address {to_email}. Please check it.')
        return redirect(reverse_lazy(settings.LOGIN_URL))

# @shared_task   
# def send_confirmation_email(request, user):
#     email_address = EmailAddress.objects.get_for_user(user, user.email)
#     # Sending confirmation
#     confirmation=EmailConfirmation.create(email_address)
#     confirmation.send(request, signup=True)