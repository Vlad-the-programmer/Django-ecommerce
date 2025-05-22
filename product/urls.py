from django.urls import path
from product import views

app_name = 'product'

urlpatterns = [
	path('products/', views.products_list_view, name='products-list'),
	path('product/<pid>/', views.product_detail_view, name='products-detail'),
	path('search/', views.search_view, name='search'),
	path('filter-product/', views.filter_product, name='filter-product'),
	# Tags
	path('products/tag/<slug:tag_slug>/', views.tags_list, name='tags'),
 
 	# Vendor
	path('vendors/', views.vendor_list_view, name='vendor-list'),
	path('vendor/<vid>/', views.vendor_detail_view, name='vendor-detail'),

	# Add Product Review
	path('ajax-add-review/<int:pid>/', views.ajax_add_review, name='ajax-add-review'),

]