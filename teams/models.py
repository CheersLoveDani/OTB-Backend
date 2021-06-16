from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    private = models.BooleanField()
    icon = models.URLField()

    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='owner_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    dps_1 = models.ForeignKey(
        'jwt_auth.User',
        related_name='dps1_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    dps_2 = models.ForeignKey(
        'jwt_auth.User',
        related_name='dps2_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    tank_1 = models.ForeignKey(
        'jwt_auth.User',
        related_name='tank1_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    tank_2 = models.ForeignKey(
        'jwt_auth.User',
        related_name='tank2_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    support_1 = models.ForeignKey(
        'jwt_auth.User',
        related_name='support1_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    support_2 = models.ForeignKey(
        'jwt_auth.User',
        related_name='support2_users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'
        