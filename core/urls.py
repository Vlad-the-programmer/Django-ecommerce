from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [

	# Homepage
	path('', views.index, name='index'),
	
	# Contact
	path('contact/', views.contact, name='contact'),

	# Ajax Contact From
	path('ajax-contact-form/', views.ajax_contact_form, name='ajax-contact-form'),

	# About Us
	path('about/', views.about, name='about'),
]