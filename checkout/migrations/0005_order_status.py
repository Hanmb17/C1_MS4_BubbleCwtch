# Generated by Django 3.2.25 on 2024-04-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New - Order received, awaiting processing'), ('processing', 'Processing - Order is being prepared for shipment'), ('shipped', 'Shipped - Order has been shipped to the customer'), ('delivered', 'Delivered - Order has been successfully delivered'), ('cancelled', 'Cancelled - Order was cancelled by customer or admin')], default='new', max_length=20),
        ),
    ]
