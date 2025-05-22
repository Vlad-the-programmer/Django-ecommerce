from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
	model = Category
	list_display = ['title', 'category_image', 'cid']

admin.site.register(Category, CategoryAdmin)
