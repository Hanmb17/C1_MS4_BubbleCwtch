from django.test import TestCase
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product

from decimal import Decimal


class TestOrderModel(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(
            name='Bubble Cwtch',
            description='Test bath bomb for bubble cwtch',
            price=6.5,
            rating=4,
            is_featured=True,
            discontinued=False,
            image_url='https://example.com/image.jpg'
        )

        self.product2 = Product.objects.create(
             name='Bubble Soap',
            description='Test soap for bubble cwtch',
            price=5,
            rating=4.2,
            is_featured=True,
            discontinued=False,
            image_url='https://example.com/image1.jpg'
        )

        self.order = Order.objects.create(
            order_number='D4F6A27E93B54C7A8E569D19234C4B1F',
            full_name="Test Person",
            email="test@email.com",
            phone_number="1234567890",
            street_address1="Test Line 1",
            street_address2="Test Line 2",
            town_or_city="Test City",
            county="Test County",
            postcode="AA11 2BB",
            country="GB",
        )

        self.order_line_item1 = OrderLineItem.objects.create(
            order=self.order,
            product=self.product1,
            quantity=1,
            lineitem_total=self.product1.price * 1,
        )

        self.order_line_item2 = OrderLineItem.objects.create(
            order=self.order,
            product=self.product2,
            quantity=2,
            lineitem_total=self.product2.price * 2,
        )


    def test_generate_order_number(self):
        """Test the _generate_order_number method"""
        order = Order()
        generated_order_number = order._generate_order_number()
        self.assertEqual(len(generated_order_number), 32)

    def test_order_string_method(self):
        """Tests the string method on the order model"""
        self.assertEqual(str(self.order), self.order.order_number)

    def test_order_number(self):
        """Test the order number"""
        self.assertEqual(self.order.order_number, 'D4F6A27E93B54C7A8E569D19234C4B1F')

    def test_order_name(self):
        """Test the order full name"""
        self.assertEqual(self.order.full_name, 'Test Person')

    def test_order_email(self):
        """Test the order email"""
        self.assertEqual(self.order.email, 'test@email.com')

    def test_order_phone(self):
        """Test the order phone"""
        self.assertEqual(self.order.phone_number, '1234567890')

    def test_order_address(self):
        """Test the order address"""
        self.assertEqual(self.order.street_address1, 'Test Line 1')
        self.assertEqual(self.order.street_address2, 'Test Line 2')
        self.assertEqual(self.order.town_or_city, 'Test City')
        self.assertEqual(self.order.county, 'Test County')
        self.assertEqual(self.order.postcode, 'AA11 2BB')
        self.assertEqual(self.order.country, 'GB')

    def test_order_total(self):
        """Test the order total on the order model"""
        expected_total = sum(item.lineitem_total
                             for item in self.order.lineitems.all())
        self.assertEqual(self.order.order_total, expected_total)

    def test_delivery_cost(self):
        """Tests the delivery cost on the order model"""
        expected_delivery_cost = Decimal('1.65').quantize(Decimal('0.01'))
        self.assertEqual(self.order.delivery_cost, expected_delivery_cost)

    def test_delivery_cost_when_total_below_threshold(self):
        """Test that delivery cost is calculated correctly when order total is below threshold"""
        # Call update_total to calculate the delivery cost
        self.order.update_total()

        # Assert that delivery cost is calculated based on the order total being below the threshold
        expected_delivery_cost = (
            self.order.order_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / Decimal('100')
        ).quantize(Decimal('0.01'))

        self.assertEqual(self.order.delivery_cost, expected_delivery_cost)

    def test_delivery_cost_when_total_above_threshold(self):
        """Test that delivery cost is zero when order total is above or equal to threshold"""
        # Create order line item with a total that is above the FREE_DELIVERY_THRESHOLD
        order_line_item1 = OrderLineItem.objects.create(
            order=self.order,
            product=self.product1,
            quantity=10,
            lineitem_total=self.product1.price * 10,
        )

        # Call update_total to calculate the delivery cost
        self.order.update_total()

        # Assert that delivery cost is zero when order total is above or equal to the threshold
        self.assertEqual(self.order.delivery_cost, Decimal('0'))

    def test_grand_total(self):
        """Tests the grand total on the order model"""
        expected_grand_total = self.order.order_total + \
            self.order.delivery_cost
        self.assertEqual(self.order.grand_total, expected_grand_total)



    def test_order_line_item_order(self):
        """Tests the order line item has the correct total"""
        self.assertEqual(self.order_line_item1.order, self.order)

    def test_order_line_item_product(self):
        """Tests the order line item has the correct product"""
        self.assertEqual(self.order_line_item1.product, self.product1)

    def test_order_line_item_quantity(self):
        """Tests the order line item has the correct quantity"""
        self.assertEqual(self.order_line_item1.quantity, 1)

    def test_order_line_item_total(self):
        """Tests the order line item has the correct total"""
        expected_line_item_total = self.order_line_item1.product.price * \
            self.order_line_item1.quantity
        self.assertEqual(self.order_line_item1.lineitem_total,
                         expected_line_item_total)

    def test_order_line_item_str(self):
        """Test the string representation of OrderLineItem"""
        expected_str = f'SKU {self.product1.name} on order {self.order.order_number}'
        actual_str = str(self.order_line_item1)
        self.assertEqual(actual_str, expected_str)


    def test_save_generates_order_number_if_not_set(self):
        """Test that save method generates order number if not set"""
        # Create a new Order instance without an order_number and save it to my database.
        new_order = Order(
            full_name="Test Person",
            email="test@email.com",
            phone_number="1234567890",
            street_address1="Test Line 1",
            street_address2="Test Line 2",
            town_or_city="Test City",
            county="Test County",
            postcode="AA11 2BB",
            country="GB",
        )

        new_order.save()

        updated_order = Order.objects.get(pk=new_order.pk)

        self.assertIsNotNone(updated_order.order_number)
        self.assertEqual(len(updated_order.order_number), 32)  