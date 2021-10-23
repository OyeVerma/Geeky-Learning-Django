from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.signals'

    def ready(self):
        import Apps.signals.signal
