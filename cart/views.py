from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string


def add_to_cart(request):
	cart_product = {}

	cart_product[str(request.GET['id'])] = {
		'qty': request.GET['qty'],
		'title': request.GET['title'],
		'price': request.GET['price'],
		'image': request.GET['image'],
		'pid': request.GET['pid'],
	}

	if 'cart_data_object' in request.session:
		if str(request.GET['id']) in request.session['cart_data_object']:
			cart_data = request.session['cart_data_object']
			cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
			cart_data.update(cart_data)
			request.session['cart_data_object'] = cart_data
		else:
			cart_data = request.session['cart_data_object']
			cart_data.update(cart_product)
			request.session['cart_data_object'] = cart_data
	else:
		request.session['cart_data_object'] = cart_product

	return JsonResponse({
			'data':request.session['cart_data_object'],
			'totalcartitems':len(request.session['cart_data_object'])
		})

def cart_view(request):
	cart_total_amount = 0
	if 'cart_data_object' in request.session:
		for product_id, item in request.session['cart_data_object'].items():
			cart_total_amount += int(item['qty']) * float(item['price'])

		return render(request, 'cart/cart.html', {
			'cart_data': request.session['cart_data_object'],
			'totalcartitems': len(request.session['cart_data_object']),
			'cart_total_amount': cart_total_amount
		})
		
	else:
		return render(request, 'cart/cart.html')

def delete_from_cart(request):
	product_id = str(request.GET['id'])
	if 'cart_data_object' in request.session:
		if product_id in request.session['cart_data_object']:
			cart_data = request.session['cart_data_object']
			del request.session['cart_data_object'][product_id]
			request.session['cart_data_object'] = cart_data

	cart_total_amount = 0
	if 'cart_data_object' in request.session:
		for product_id, item in request.session['cart_data_object'].items():
			cart_total_amount += int(item['qty']) * float(item['price'])

	context = render_to_string('cart/async/cart-list.html', {
			'cart_data': request.session['cart_data_object'],
			'totalcartitems': len(request.session['cart_data_object']),
			'cart_total_amount': cart_total_amount
		})
	return JsonResponse({
			'data': context,
			'totalcartitems': len(request.session['cart_data_object']),
		})

def update_cart(request):
	product_id = str(request.GET['id'])
	product_qty = request.GET['qty']
	if 'cart_data_object' in request.session:
		if product_id in request.session['cart_data_object']:
			cart_data = request.session['cart_data_object']
			cart_data[str(request.GET['id'])]['qty'] = product_qty
			request.session['cart_data_object'] = cart_data

	cart_total_amount = 0
	if 'cart_data_object' in request.session:
		for product_id, item in request.session['cart_data_object'].items():
			cart_total_amount += int(item['qty']) * float(item['price'])


	context = render_to_string('cart/async/cart-list.html', {
			'cart_data': request.session['cart_data_object'],
			'totalcartitems': len(request.session['cart_data_object']),
			'cart_total_amount': cart_total_amount
		})
	return JsonResponse({
			'data': context,
			'totalcartitems': len(request.session['cart_data_object']),
		})

