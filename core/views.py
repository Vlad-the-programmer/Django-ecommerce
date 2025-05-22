from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F, ExpressionWrapper, DecimalField
from core.models import ContactUs
from product.models import Product


def index(request):
	products = Product.objects.filter(IsActive=True)

	special_offers = products.filter(featured=True).annotate(
		discount_percentage=ExpressionWrapper(
			((F('old_price') - F('price')) / F('old_price')) * 100,
			output_field=DecimalField()
		)
    ).order_by('-discount_percentage')[:9]
    
	oldest_products = products.order_by('date')

	context = {
		"products": products,
		"special_offers": special_offers,
		"oldest_products": oldest_products,
	}
	return render(request, 'core/index.html', context)


def contact(request):
	return render(request, 'core/contact.html')

def ajax_contact_form(request):
	name = request.GET['name']
	email = request.GET['email']
	message = request.GET['message']

	ContactUs.objects.create(
		name=name,		
		email=email,		
		message=message,		
	)

	data = {
		'bool': True,
	}

	return JsonResponse({'data': data})

def about(request):
	return render(request, 'core/about.html')
