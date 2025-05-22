from django.urls import path
from core import views

app_name = 'category'

urlpatterns = [
	# Category
	path('category/', views.category_list_view, name='category-list'),
	path('category/<cid>/', views.category_product_list_view, name='category-product-list'),
]