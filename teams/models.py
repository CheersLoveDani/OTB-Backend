from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    private = models.BooleanField()
    icon = models.URLField()

    def __str__(self):
        return self.name