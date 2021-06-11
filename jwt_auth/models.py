
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50)
    battletag = models.CharField(max_length=50)
    sr = models.IntegerField(
        default=2500,
        validators=[MinValueValidator(0), MaxValueValidator(5000)]
    )
    