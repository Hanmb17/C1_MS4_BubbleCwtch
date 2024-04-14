from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm


# Create your views here.

def all_products(request):
    """ A view to show all products, inclusind sorting and search queries """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction =request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'


            products = products.order_by(sortkey)

    

        if'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = Category.objects.get(name=category)

            print(category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't search for anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    print(current_sorting)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def add_product(request):
    """ Add a new product to the store """
    form = ProductForm()

    # Sets page template
    template = 'products/add_product.html'

    # Sets form content
    context = {
        'form': form,
    }

    return render(request, template, context)