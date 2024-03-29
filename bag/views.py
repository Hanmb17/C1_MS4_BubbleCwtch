from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

def update_bag(request):
    """ Updates the shopping bag contents """
    if request.method == 'POST':
        
        item_id = request.POST.get('item_id')
        new_quantity = int(request.POST.get('quantity'))

        bag = request.session.get('bag', {})

        if item_id in bag:
            if new_quantity > 0:
                bag[item_id] = new_quantity
            else:
                del bag[item_id]
                messages.success(request, 'Item removed from bag.')
        else:
            messages.error(request, 'Item not found in bag.')

        request.session['bag'] = bag

    return redirect(reverse('view_bag'))
