from django.contrib import admin
from product.models import Product, ProductImages, ProductReview, Vendor

class ProductImagesAdmin(admin.TabularInline):
	model = ProductImages

class ProductAdmin(admin.ModelAdmin):
	model = Product
	inlines = [ProductImagesAdmin]
	list_display = ['user', 'title', 'product_image', 'price','category', 'vendor', 'featured', 'IsActive', 'pid']

class ProductReviewAdmin(admin.ModelAdmin):
	model = Product
	list_display = ['user', 'product', 'rating']
 

class VendorAdmin(admin.ModelAdmin):
	list_display = ['name', 'vendor_image', 'pid', 'IsActive']
 
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Product, ProductAdmin)
