from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TravelApp.accounts'

    def ready(self):
        import TravelApp.accounts.signals

