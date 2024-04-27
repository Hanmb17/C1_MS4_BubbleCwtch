from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from .models import Category, Product


class TestProductsViews(TestCase):
    """ Test home url views """

    def setUp(self):
        """ Create sample categories  """
        self.bath_bombs_category = Category.objects.create(
            name='bath_bombs',
            friendly_name='Bath Bombs'
        )

        self.soaps_category = Category.objects.create(
            name='soaps',
            friendly_name='Soaps'
        )

        self.shower_jellies_category = Category.objects.create(
            name='shower_jellies',
            friendly_name='Shower Jellies'
        )

        """ Create a sample product for testing the detail view  """
        self.test_product = Product.objects.create(
            category=self.bath_bombs_category,
            name='Test Bathbomb',
            description='Test description for bath bomb',
            price=6.00,
            rating=3,
            is_featured=False,
            discontinued=False,
            image_url='https://example.com/image.jpg'
        )

        self.product_without_image = Product.objects.create(
            name='Product Without Image',
            description='Description of product without image',
            price=5.00
        )

        self.soap_product = Product.objects.create(
            category=self.soaps_category,
            name='Test Soap',
            description='Test description for soap',
            price=4.00
        )

        self.shower_jellies_product = Product.objects.create(
            category=self.shower_jellies_category,
            name='Test Shower Jelly',
            description='Test description for shower jelly',
            price=4.00
        )

    def test_get_products_page(self):
        """ Test products view  """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_view_with_invalid_id(self):
        """ Test the product detail view with an invalid product id  """
        response = self.client.get(reverse('product_detail', args=['999']))
        self.assertEqual(response.status_code, 404)

    def test_product_detail_view_with_valid_id(self):
        """ Test the product detail view with a valid product id."""
        response = self.client.get(
            reverse('product_detail', args=[self.test_product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_view_without_image(self):
        """
        Test that the product detail view
        handles a product without an image.
        """
        response = self.client.get(
            reverse('product_detail', args=[self.product_without_image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no_image.png')

    def test_product_card_classes(self):
        """
        Test that product cards have correct
        CSS classes based on category.
        """
        response = self.client.get(reverse('products'))

        # Check if the product card classes are correct for each product
        # Check for bath bomb product class
        self.assertContains(response, 'bg-purple', count=1)
        # Check for soap product class
        self.assertContains(response, 'bg-blue', count=1)
        # Check for shower jelly product class
        self.assertContains(response, 'bg-green', count=1)

    def test_search_query(self):
        """ Test search functionality """

        Product.objects.create(
            category=self.soaps_category,
            name='Lavender Soap',
            description='Test description for lavender soap',
            price=5.00
        )

        response = self.client.get(reverse('products') + '?q=Lavender')

        self.assertContains(response, 'Lavender Soap')

    def test_empty_query(self):
        """ Test handling of empty search query """

        response = self.client.get(reverse('products') + '?q=')

        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("You didn't search for anything!", messages)
        self.assertEqual(response.status_code, 302)
