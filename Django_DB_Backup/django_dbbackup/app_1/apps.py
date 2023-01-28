from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_1'
    def ready(self):
        from app_1.api.scheduler import scheduler
        scheduler.start()
