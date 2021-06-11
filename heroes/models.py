from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=50)
    img_large = models.URLField()
    img_banner = models.URLField()

    DPS = 'DPS'
    TANK = 'TANK'
    SUPPORT = 'SUPPORT'
    ROLE_CHOICES = [
        (DPS, 'dps'),
        (TANK, 'tank'),
        (SUPPORT, 'support')
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=DPS
    )

    def __str__(self):
        return self.name