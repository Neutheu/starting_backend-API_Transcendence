from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_games')
    players = models.ManyToManyField(User, related_name='joined_games')
    status = models.CharField(
        max_length=50,
        choices=[('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('FINISHED', 'Finished')],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
