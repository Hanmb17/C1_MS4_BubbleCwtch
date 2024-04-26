from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Add/Edit Product Form
    """

    class Meta:
        model = Product
        exclude = ('rating',)

        labels = {
            'category': 'Product Category',
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'image_url': 'Image URL',
            'is_featured': 'Featured?',
            'discontinued': 'Discontinue Product?'
        }

    # Set image field attributes
    image = forms.ImageField(
        label='Product Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get all categories and assign their friendly name to the select input
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            # Adds styling classes to inputs
            if field_name not in [
                'is_featured',
                'discontinued',
                'image',
            ]:
                field.widget.attrs['class'] = (
                        'input-form mb-3 px-2 py-2 text-grey rounded-2')

            if field_name in ['is_featured', 'delivery_charge']:
                field.widget.attrs['class'] = "form-check-input m-0"

            if field_name == 'discontinued':
                field.widget.attrs['class'] = (
                    "form-check-input")
