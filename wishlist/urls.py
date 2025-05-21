
from django.urls import path
from core import views

app_name = 'wishlist'

urlpatterns = [

	path('wishlist/', views.wishlist_view, name='wishlist'),
	path('add-to-wishlist/', views.add_to_wishlist, name='add-to-wishlist'),
	path('remove-from-wishlist/', views.remove_from_wishlist, name='remove-from-wishlist'),

]