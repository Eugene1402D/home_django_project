from django.apps import AppConfig


# класс конфигурации используется для настройки приложения Django
class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"
    verbose_name = 'Предложения и акции'
