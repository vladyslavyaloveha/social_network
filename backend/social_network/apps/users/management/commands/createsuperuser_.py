import structlog
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a superuser with a password non-interactively"
    _logger = structlog.get_logger("logger")

    def add_arguments(self, parser):
        parser.add_argument("--username", help="Username")
        parser.add_argument("--email", help="Email")
        parser.add_argument("--password", help="Password")

    def handle(self, *args, **options):
        user = get_user_model()
        if not user.objects.filter(username=options["username"]).exists():
            username = options["username"]
            email = options["email"]
            self._logger.info("superuser created", username=username, email=email)
            user.objects.create_superuser(
                username=username, email=email, password=options["password"]
            )
