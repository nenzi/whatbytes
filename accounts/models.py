from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass  # Extend in the future if needed
