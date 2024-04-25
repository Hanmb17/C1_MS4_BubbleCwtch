from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
        Import signals module when the app is ready.
    """

    name = 'checkout'

    def ready(self):
        import checkout.signals
