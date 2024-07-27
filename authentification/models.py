from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_gerant = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Client(CustomUser):
    pass

class Gerant(CustomUser):
    pass

    def save(self, *args, **kwargs):
        self.is_gerant = True
        super().save(*args, **kwargs)