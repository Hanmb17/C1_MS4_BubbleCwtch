from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.forms import OrderStatusUpdateForm

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please check the form.')
    else:
        form = UserProfileForm(instance=profile)
    
    if request.user.is_superuser:
        # Superuser sees all orders sorted by date (most recent first)
        orders = Order.objects.order_by('-date')

        # Filter orders by status if status is provided in the request
        status = request.GET.get('status')
        if status:
            orders = orders.filter(status=status)
    else:
        orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    """ Displays the order history using the checkout_success template """
    order = get_object_or_404(Order, order_number=order_number)

    if request.method == 'POST' and request.user.is_superuser:
        # Handle status update form submission
        form = OrderStatusUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order status updated successfully')
        else:
            messages.error(
                request, 'Order status Update failed. Please check the form.')
    else:
        # Initialize form with order instance
        form = OrderStatusUpdateForm(instance=order)

    context = {
        'order': order,
        'form': form,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)