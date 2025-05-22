from django.contrib import admin
from wishlist.models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
	model = Wishlist
	list_display = ['user', 'product', 'created_at']
 
admin.site.register(Wishlist, WishlistAdmin)
