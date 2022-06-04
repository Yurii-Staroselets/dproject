from django.shortcuts import render, get_object_or_404
from .models import Category1, Category2, Category3, Product


def categories(request):
    return {
        'categories': Category1.objects.all()
    }


def brand(request):
    return {
        'brand': Category2.objects.all()
    }


def algorith(request):
    return {
        'algorith': Category3.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category1, slug=category_slug)
    products = Product.objects.filter(category1=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/detail.html', {'product': product})

