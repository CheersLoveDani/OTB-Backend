
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

    dps_1 = models.ForeignKey(
        'heroes.Hero',
        related_name='dps1_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be dps',
        on_delete=models.SET_NULL
    )
    dps_2 = models.ForeignKey(
        'heroes.Hero',
        related_name='dps2_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be dps',
        on_delete=models.SET_NULL
    )
    dps_3 = models.ForeignKey(
        'heroes.Hero',
        related_name='dps3_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be dps',
        on_delete=models.SET_NULL
    )

    tank_1 = models.ForeignKey(
        'heroes.Hero',
        related_name='tank1_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be tank',
        on_delete=models.SET_NULL
    )
    tank_2 = models.ForeignKey(
        'heroes.Hero',
        related_name='tank2_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be tank',
        on_delete=models.SET_NULL
    )
    tank_3 = models.ForeignKey(
        'heroes.Hero',
        related_name='tank3_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be tank',
        on_delete=models.SET_NULL
    )

    support_1 = models.ForeignKey(
        'heroes.Hero',
        related_name='support1_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be support',
        on_delete=models.SET_NULL
    )
    support_2 = models.ForeignKey(
        'heroes.Hero',
        related_name='support2_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be support',
        on_delete=models.SET_NULL
    )
    support_3 = models.ForeignKey(
        'heroes.Hero',
        related_name='support3_heroes',
        blank=True,
        null=True,
        help_text='Must be unique, must be support',
        on_delete=models.SET_NULL
    )
