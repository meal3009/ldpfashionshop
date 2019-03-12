from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
from .models import Product,Banner,Category

# Create your views here.
def index(request):
    products1 = Product.objects.order_by('-id').filter(category=1,published=True)[:10]
    products2 = Product.objects.order_by('-id').filter(category=2,published=True)[:10]
    products3 = Product.objects.order_by('-id').filter(category=3,published=True)[:10]
    products4 = Product.objects.order_by('-id').filter(category=4,published=True)[:10]
    categorys = Category.objects.all()
    banners = Banner.objects.all()

    context = {
        'products1' : products1,
        'products2' : products2,
        'products3' : products3,
        'products4' : products4,
        'banners' : banners,
        'categorys' : categorys
    }
    return render(request,'shop/index.html',context)

def outer(request):
    product = Product.objects.order_by('-id').filter(category=1,published=True)
    categorys = Category.objects.all()

    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'product' : paged_listings,
        'categorys' : categorys,
    }
    return render(request,'shop/categorys.html',context)

def top(request):
    product = Product.objects.order_by('-id').filter(category=2,published=True)
    categorys = Category.objects.all()

    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'product' : paged_listings,
        'categorys' : categorys,
    }
    return render(request,'shop/categorys.html',context)

def dress(request):
    product = Product.objects.order_by('-id').filter(category=3,published=True)
    categorys = Category.objects.all()

    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'product' : paged_listings,
        'categorys' : categorys,
    }
    return render(request,'shop/categorys.html',context)

def pants(request):
    product = Product.objects.order_by('-id').filter(category=4,published=True)
    categorys = Category.objects.all()

    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'product' : paged_listings,
        'categorys' : categorys,
    }
    return render(request,'shop/categorys.html',context)

def product(request, products_id):
    product = get_object_or_404(Product, pk=products_id)

    context ={
        'product': product
    }
    return render(request, 'shop/product.html',context)

def search(request):
    product = Product.objects.order_by('-id').filter(published=True)
    search = request.GET['search']
    if search:
        product = Product.objects.filter(Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(price__icontains=search) |
                Q(code__icontains=search))
    paginator = Paginator(product, 12)
    page = request.GET.get('page')

    try:
        paged_listings = paginator.page(page)
    except PageNotAnInteger:
        paged_listings = paginator.page(1)
    except EmptyPage:
        paged_listings = paginator.page(paginator.num_pages)

    context = {
        'product' : paged_listings,
        'search' : search,
    }

    return render(request,'shop/search.html',context)
