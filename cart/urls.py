
from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
	path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
	path('cart/', views.cart_view, name='cart'),
	path('delete-from-cart/', views.delete_from_cart, name='delete-from-cart'),
	path('update-cart/', views.update_cart, name='update-cart'),

]