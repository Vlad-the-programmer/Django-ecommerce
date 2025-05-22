from django.contrib import admin
from blog.models import Post, PostCategory, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'blog_image', 'pid']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'cid']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)