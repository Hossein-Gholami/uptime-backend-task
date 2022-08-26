from django.apps import AppConfig


class UptimeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "uptime"

    # def ready(self):
    #     import uptime.signals
