from django.shortcuts import (
    render, 
    redirect,  
    HttpResponse,
    get_object_or_404
    )
from django.urls import reverse
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product =Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

def update_bag(request):
    """ Updates the shopping bag contents """
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        product = get_object_or_404(Product, pk=item_id)
        new_quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if item_id in bag:
            if new_quantity > 0:
                bag[item_id] = new_quantity
                messages.success(request, f'Updated {product.name} quantity to {new_quantity}')
            else:
                del bag[item_id]
                messages.success(request, f'{product.name} removed from bag.')
        else:
            messages.error(request, f'{product.name} not found in bag.')

        request.session['bag'] = bag

    return redirect(reverse('view_bag'))
            

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)

        bag = request.session.get('bag', {})

        bag.pop(item_id)
        request.session['show_bag_summary'] = True
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
