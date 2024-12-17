from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "DishcoveryApp.accounts"

    def ready(self):
        import DishcoveryApp.accounts.signals
