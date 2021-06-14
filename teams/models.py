from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    private = models.BooleanField()
    icon = models.URLField()

    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='owner_users',
        on_delete=models.CASCADE,
    )

    dps1 = models.ForeignKey(
        'jwt_auth.User',
        related_name='dps1_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    dps2 = models.ForeignKey(
        'jwt_auth.User',
        related_name='dps2_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    tank1 = models.ForeignKey(
        'jwt_auth.User',
        related_name='tank1_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    tank2 = models.ForeignKey(
        'jwt_auth.User',
        related_name='tank2_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    support1 = models.ForeignKey(
        'jwt_auth.User',
        related_name='support1_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    support2 = models.ForeignKey(
        'jwt_auth.User',
        related_name='support2_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
        