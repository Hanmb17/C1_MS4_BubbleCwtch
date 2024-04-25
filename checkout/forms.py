from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for Order Model
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Sets placeholder values for form inputs
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Sets autofocus on first input
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Adds placeholders to inputs (except Country)
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds styling classes to all inputs
            self.fields[field].widget.attrs['class'] = (
                'input-form mb-3 px-2 py-2 text-grey rounded-2')


class OrderStatusUpdateForm(forms.ModelForm):
    """
    Form for updating the status of an Order model instance.
    Only intended to be used by admin.
    """

    class Meta:
        model = Order
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({
            'class': 'input-form mb-3 mt-2 px-2 py-2 text-grey rounded-2'})
