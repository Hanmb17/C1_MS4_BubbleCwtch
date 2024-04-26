from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin view for the UserProfile model.
    """
    fields = (
        'user', 'default_phone_number', 'default_street_address1',
        'default_street_address2', 'default_town_or_city', 'default_county',
        'default_postcode', 'default_country',
    )

    list_display = (
        'user', 'default_phone_number', 'default_street_address1',
        'default_street_address2', 'default_town_or_city', 'default_county',
        'default_postcode', 'default_country',
    )

    # Define fields to be searchable in the admin interface
    search_fields = (
        'user', 'default_phone_number', 'default_street_address1',
        'default_street_address2', 'default_town_or_city', 'default_county',
        'default_postcode', 'default_country',
    )


admin.site.register(UserProfile, UserProfileAdmin)
