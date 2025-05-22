from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
from django.template.loader import render_to_string
from product.models import Product, ProductReview, Vendor
from product.forms import ProductReviewFrom
from taggit.models import Tag

def products_list_view(request):
	products = Product.objects.filter(product_status='published')
	context = {
		"products": products
	}
	return render(request, 'products/product-list.html', context)


def vendor_list_view(request):
	vendors = Vendor.objects.all()
	context = {
		'vendors': vendors,
	}
	return render(request, 'products/vendor-list.html', context)

def vendor_detail_view(request, vid):
	vendor = Vendor.objects.get(vid=vid)
	products = Product.objects.filter(product_status='published', vendor=vendor)
	context = {
		'vendor': vendor,
		'products': products,
	}
	return render(request, 'products/vendor-detail.html', context)

def product_detail_view(request, pid):
	product = Product.objects.get(pid=pid)
	# product = get_object_or_404(Product, pid=pid)
	products = Product.objects.filter(category=product.category).exclude(pid=pid)
	p_image = product.p_images.all()

	reviews = ProductReview.objects.filter(product=product).order_by('-date')
	average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
	review_form = ProductReviewFrom()

	allow_add_review = True
	if request.user.is_authenticated:
		user_review_count = ProductReview.objects.filter(user=request.user, product=product).count() 

		if user_review_count > 0:
			allow_add_review = False

	context = {
		'product': product,
		'p_image': p_image,
		'products': products,
		'reviews': reviews,
		'average_rating': average_rating,
		'review_form': review_form,
		'allow_add_review': allow_add_review,
	}
	return render(request, 'products/product-detail.html', context)

def tags_list(request, tag_slug=None):
	products = Product.objects.filter(product_status='published').order_by('-id')

	tag = None
	if tag_slug:
		tag = Tag.objects.get(slug=tag_slug)
		# tag = get_object_or_404(Tag, slug=tag_slug)
		products = products.filter(tags__in=[tag])

	context = {
		'products': products,
		'tag': tag,
	}

	return render(request, 'products/tag.html', context)

def ajax_add_review(request, pid):
	product = Product.objects.get(pk=pid)
	user = request.user
	image = user.imageURL

	review = ProductReview.objects.create(
		user=user,
		product=product,
		review=request.POST['review'],
		rating=request.POST['rating'],
	)
	
	context = {
		'user': user.username,
		'review': request.POST['review'],
		'rating': request.POST['rating'],
		'image': image
	}

	average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))


	return JsonResponse(
		{
			'bool': True,
			'context': context,
			'average_reviews': average_reviews,
		}
	)

def search_view(request):
	# query = request.GET['q'] OR
	query = request.GET.get('q') 

	products = Product.objects.filter(title__icontains=query).order_by('-date')

	context = {
		'products': products,
		'query': query,
	}

	return render(request, 'products/search.html', context)

def filter_product(request):
	categories = request.GET.getlist('category[]')
	vendors = request.GET.getlist('vendor[]')

	min_price = request.GET.get('min_price')
	max_price = request.GET.get('max_price')

	products = Product.objects.filter(product_status='published').order_by('-id').distinct()

	products = products.filter(price__gte=min_price)
	products = products.filter(price__lte=max_price)

	if len(categories) > 0:
		products = products.filter(category__id__in=categories).distinct()
	if len(vendors) > 0:
		products = products.filter(vendor__id__in=vendors).distinct()

	context = {
		'products': products
	}

	data = render_to_string('products/async/product-list.html', context)
	return JsonResponse({'data': data})

