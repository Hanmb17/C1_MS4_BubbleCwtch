from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    # Retrieve all products marked as featured
    featured_products = Product.objects.filter(is_featured=True)

    context = {
        'products': featured_products,
    }

    return render(request, 'home/index.html', context)
