from django.apps import AppConfig


class LottopyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lottopy'
    def ready(self):
        # Initialize celery
        import lottopy.celery
