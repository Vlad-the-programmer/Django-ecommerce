from django.contrib import admin
from core.models import  ContactUs


# class AddressAdmin(admin.ModelAdmin):
# 	list_display = ['user', 'address', 'status']

class ContactUsAdmin(admin.ModelAdmin):
	model = ContactUs
	list_display = ['name', 'email']

# admin.site.register(Address, AddressAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
