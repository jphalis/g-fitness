from django.shortcuts import render, Http404

from .models import Product, ProductImage

# Create your views here.


def massage(request):
    return render(request, 'massage.html', {})


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {
            'query': q,
            'products': products
        }
        template = 'products/results.html'
    else:
        context = {}
        template = 'products/products.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        images = ProductImage.objects.filter(product=product)
        context = {
            'product': product,
            'images': images
        }
        return render(request, 'products/single.html', context)
    except:
        raise Http404
