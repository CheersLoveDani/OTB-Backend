
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

    DPS = 'DPS'
    TANK = 'TANK'
    SUPPORT = 'SUPPORT'
    ROLE_CHOICES = [
        (DPS, 'dps'),
        (TANK, 'tank'),
        (SUPPORT, 'support')
    ]
    mainrole = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=DPS
    )

    dps1 = models.ForeignKey(
        'heroes.Hero',
        related_name='dps1_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be dps',
        on_delete=models.SET_NULL
    )
    dps2 = models.ForeignKey(
        'heroes.Hero',
        related_name='dps2_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be dps',
        on_delete=models.SET_NULL
    )
    dps3 = models.ForeignKey(
        'heroes.Hero',
        related_name='dps3_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be dps',
        on_delete=models.SET_NULL
    )

    tank1 = models.ForeignKey(
        'heroes.Hero',
        related_name='tank1_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be tank',
        on_delete=models.SET_NULL
    )
    tank2 = models.ForeignKey(
        'heroes.Hero',
        related_name='tank2_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be tank',
        on_delete=models.SET_NULL
    )
    tank3 = models.ForeignKey(
        'heroes.Hero',
        related_name='tank3_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be tank',
        on_delete=models.SET_NULL
    )

    support1 = models.ForeignKey(
        'heroes.Hero',
        related_name='support1_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be support',
        on_delete=models.SET_NULL
    )
    support2 = models.ForeignKey(
        'heroes.Hero',
        related_name='support2_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be support',
        on_delete=models.SET_NULL
    )
    support3 = models.ForeignKey(
        'heroes.Hero',
        related_name='support3_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be support',
        on_delete=models.SET_NULL
    )
