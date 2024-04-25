from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from .models import Order


class CheckoutViewTestCase(TestCase):
    """
    Order Views Tests
    """
    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')

        # Create a test product
        self.productTest = Product.objects.create(
            name='Test Product',
            description='Test Product Description',
            price=10,
            rating=4,
            is_featured=True,
            discontinued=False,
            image_url='https://example.com/image.jpg'
        )

    def test_get_checkout_page_with_empty_bag(self):
        """Test checkout page redirects to products with empty bag."""
        response = self.client.get(self.checkout_url)
        self.assertRedirects(response, '/products/')

    def test_get_checkout_page_with_bag_items(self):
        """Test checkout page view with bag items."""
        # Simulate bag items in the session
        session = self.client.session
        session['bag'] = {str(self.productTest.id): 1}
        session.save()

        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
