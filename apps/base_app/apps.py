from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.base_app"
