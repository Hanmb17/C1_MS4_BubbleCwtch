from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)


class Category(models.Model):
    """
    Category Model
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(
        max_length=254
        )

    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )

    def __str__(self):
        """ String representation of Category name """
        return self.name

    def get_friendly_name(self):
        """ Model Method to return friendly_name """
        return self.friendly_name


class Product(models.Model):
    """
    Product Model
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    name = models.CharField(
        max_length=254
        )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
        )

    rating = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(5, message="Must be between 0-5"),
            MinValueValidator(0, message="Must be between 0-5")
        ],
    )

    is_featured = models.BooleanField(
        default=False,
        blank=True
        )

    discontinued = models.BooleanField(
        default=False,
        blank=True
        )

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
        )

    image = models.ImageField(
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name
