from django.shortcuts import render
from core.models import Product
from category.models import Category

def category_list_view(request):
	categories = Category.objects.all()
	context = {
		"categories": categories,
	}
	return render(request,  'productCategory/category-list.html', context)

def category_product_list_view(request, cid):
	category = Category.objects.get(cid=cid)
	products = Product.objects.filter(IsActive=True, category=category)
	context = {
		"category": category,
		"products": products,
	}
	return render(request, 'productCategory/category-products-list.html', context)
