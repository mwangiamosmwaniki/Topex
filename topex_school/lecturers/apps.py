from django.apps import AppConfig

class LecturersConfig(AppConfig):
    name = 'lecturers'

    def ready(self):
        import lecturers.signals
